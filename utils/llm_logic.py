import streamlit as st
import google.generativeai as genai

# --- Configure Gemini API ---
api_key = st.secrets.get("GEMINI_API_KEY", None)

if api_key:
    genai.configure(api_key=api_key)

def get_gemini_response(user_input, system_context):
    try:
        api_key = st.secrets.get("GEMINI_API_KEY", None)
        if not api_key:
            return "AI is currently offline. But here’s what you should do: " + system_context

        genai.configure(api_key=api_key)

        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        You are VoterOS, a smart civic assistant.

        User situation:
        {system_context}

        User question:
        {user_input}

        Your job:
        - Explain clearly what is happening
        - Tell the user what they should do next
        - Keep it simple, helpful, and under 3 sentences
        """

        response = model.generate_content(prompt)
        return response.text
        return response.text

    except Exception:
        return "System Update: " + system_context

def process_input(user_input):
    text = user_input.lower()
    m = st.session_state.milestones
    current_status = ""

    # --- Scenario Simulator Detection ---
    if any(w in text for w in ["what if", "if i", "suppose", "miss", "late", "peak", "forget", "happen"]):
        if "register" in text or "miss" in text or "deadline" in text:
            st.session_state.scenario_query = "missed_registration"
            return "User asked 'what if' about missing registration. Triggered consequence in the Scenario Simulator."
            
        elif "time" in text or "10 am" in text or "peak" in text or "late" in text or "crowd" in text:
            st.session_state.scenario_query = "peak_hour"
            return "User asked 'what if' about timing/peak hours. Triggered wait time warnings in Scenario Simulator."
            
        elif "id" in text or "forget" in text or "no document" in text or "lose" in text:
            st.session_state.scenario_query = "no_id"
            st.session_state.progress = min(st.session_state.get("progress", 0), 75) # Block 100% readiness
            return "User asked 'what if' about forgetting ID. Triggered ID alternatives in Scenario Simulator."
            
        elif "move" in text or "relocate" in text:
            st.session_state.scenario_query = "relocation"
            st.session_state.required_form = "Form 8 (Shifting of Residence)"
            return "User asked 'what if' about relocating. Triggered Form 8 path in Scenario Simulator."
    else:
        st.session_state.scenario_query = None

    # --- Geo-Targeted Phase Detection ---
    if "delhi" in text or "new delhi" in text:
        st.session_state.phase = "Phase 6"
        st.session_state.vote_date = "May 25, 2026"
        current_status = "Detected user is in Delhi (Phase 6). Warn them about the upcoming May 25th deadline."
    elif "mumbai" in text or "maharashtra" in text:
        st.session_state.phase = "Phase 5"
        st.session_state.vote_date = "May 20, 2026"
        current_status = "Detected user is in Mumbai (Phase 5). Vote date is May 20."
    elif "nri" in text or "abroad" in text or "dubai" in text:
        st.session_state.required_form = "Form 6A (Overseas Indian Voter)"
        st.session_state.progress = 50
        current_status = "Detected NRI/Overseas voter. They MUST use Form 6A, not Form 6."

    # STEP 1: Check Eligibility
    if not m["eligible"]:
        if any(word in text for word in ["yes", "yeah", "18", "older", "i am", "yup"]):
            st.session_state.milestones["eligible"] = True
            st.session_state.progress = 25
            current_status = "User is 18+ and eligible. Consequence: They can proceed to registration. Next Step: Ask what city they currently live in."
        elif any(word in text for word in ["no", "17", "under"]):
            current_status = "User is under 18. Consequence: Cannot vote in this cycle. Next Step: Tell them about advance application."
        else:
            current_status = "Clarify if they are an Indian citizen aged 18 or older."

    # STEP 2: Check Registration
    elif m["eligible"] and not m["has_voter_id"]:
        if any(word in text for word in ["yes", "i do", "have it", "yup"]):
            st.session_state.milestones["has_voter_id"] = True
            st.session_state.progress = 50
            current_status = "User has Voter ID. Consequence: Form 6 is not needed. Next Step: Ask if their address is current or if they shifted."
        elif any(word in text for word in ["no", "don't", "do not"]):
            if st.session_state.get("required_form") != "Form 6A (Overseas Indian Voter)":
                st.session_state.required_form = "Form 6 (New Voter Registration)"
            st.session_state.progress = 50
            current_status = f"User needs {st.session_state.required_form} because they are not registered. Consequence: They must wait until the next cycle if they miss the deadline. Next Step: Ask them to confirm their city and if they have Aadhaar or PAN."
        else:
            current_status = "Ask if they have a registered Voter ID."

    # STEP 3: Address / Edge Cases
    elif m["has_voter_id"] and not m["address_correct"]:
        if any(word in text for word in ["moved", "shifted", "new city", "no", "incorrect"]):
            st.session_state.required_form = "Form 8 (Shifting of Residence)"
            st.session_state.progress = 75
            st.session_state.milestones["address_correct"] = True
            current_status = "User requires Form 8 because their address changed. Consequence: You cannot vote at the new location until updated. Next Step: Confirm what city they moved to and what ID they will bring."
        elif any(word in text for word in ["yes", "correct", "same", "yup"]):
            st.session_state.milestones["address_correct"] = True
            st.session_state.required_form = "None! You are registered."
            st.session_state.progress = 75
            current_status = "User address is correct. Consequence: No forms required. Next Step: Ask them to confirm their city/state and name ONE ID they will bring."
        else:
            current_status = "Ask if their address perfectly matches their Voter ID."

    # STEP 4: Document Verification
    elif m["address_correct"] or "Form 6" in st.session_state.get("required_form", ""):
        if any(doc in text for doc in ["aadhaar", "pan", "passport"]):
            if "aadhaar" in text: st.session_state.docs["Aadhaar"] = True
            if "pan" in text: st.session_state.docs["PAN Card"] = True
            if "passport" in text: st.session_state.docs["Passport"] = True
            st.session_state.progress = 100
            current_status = "User provided approved ID. Consequence: They are fully ready. Next Step: Tell them to check their specific Election Phase timeline on the dashboard."
        else:
            current_status = "User missing valid ID. Consequence: You will not be allowed inside the polling booth. Next Step: Remind them to select Aadhaar, PAN, or Passport."
            
    else:
        current_status = "Gently guide them back to the voting process."

    return current_status