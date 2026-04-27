import streamlit as st

def init_state():
    if "messages" not in st.session_state:
        # The AI takes the lead immediately so the user knows what to do!
        st.session_state.messages = [
            {"role": "assistant", "content": "Welcome to VoterOS! Let's get you ready for the upcoming elections. First, are you an Indian citizen over the age of 18?"}
        ]

    # Track actual completion milestones
    if "milestones" not in st.session_state:
        st.session_state.milestones = {
            "eligible": False,
            "has_voter_id": False,
            "address_correct": False
        }

    if "progress" not in st.session_state:
        st.session_state.progress = 0

    if "steps" not in st.session_state:
        st.session_state.steps = ["Eligibility", "Registration", "Preparation", "Voting Day"]

    if "required_form" not in st.session_state:
        st.session_state.required_form = "Pending..."
        
    if "docs" not in st.session_state:
        st.session_state.docs = {"Aadhaar": False, "PAN Card": False, "Passport": False}