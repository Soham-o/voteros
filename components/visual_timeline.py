import streamlit as st

def render_timeline():
    # --- Geo-Targeted Election Tracker & Alerts ---
    current_form = st.session_state.get("required_form", "Pending...")
    phase = st.session_state.get("phase", None)
    vote_date = st.session_state.get("vote_date", None)
    
    if phase and vote_date:
        st.success(f"📍 **Location Locked:** Your constituency votes in **{phase}**.")
        st.markdown(f"""
        <div style='background: linear-gradient(90deg, #1A1C23 0%, #0E1117 100%); padding: 20px; border-radius: 10px; border-left: 5px solid #00FFFF;'>
            <h3 style='margin:0; color:#00FFFF;'>Countdown to {phase}</h3>
            <h1 style='margin:0; font-size: 2.5rem; color:white;'>{vote_date}</h1>
            <p style='color:#888; margin-top:5px;'>The Model Code of Conduct is currently active in your region.</p>
        </div>
        <br>
        """, unsafe_allow_html=True)
    elif current_form != "Pending...":
        st.info(f"🧠 **AI Detected:** {current_form} required based on your profile.")

    if "Form 6A" in current_form:
        st.error("✈️ **NRI Status Detected:** Standard voting rules do not apply. You must use the Overseas Portal.")
    elif "Form 8" in current_form:
        st.warning("🔀 **Alternate Path Activated:** Address Update Required before Voting.")
        
    st.markdown("---")

    # --- Confidence Engine Panel ---
    st.subheader("🎯 Confidence Engine")
    
    prog = st.session_state.progress
    missing_text = "None"
    next_action = "Go Vote!"
    
    if prog < 25:
        missing_text = "Eligibility Confirmation"
        next_action = "Confirm Age & Citizenship in chat"
    elif prog < 50:
        missing_text = "Voter ID Status"
        next_action = "Verify NVSP Registration"
    elif prog < 75:
        form = st.session_state.get("required_form", "")
        missing_text = "Address Verification"
        next_action = f"Submit {form}" if "Form" in form else "Confirm Current Address"
    elif prog < 100:
        missing_text = "Approved ID Proof"
        next_action = "Confirm Polling ID (Aadhaar/PAN/Passport)"

    st.markdown(f"""
    <div style='background-color: #161A22; padding: 15px; border-radius: 8px; border-left: 5px solid #00FFFF; display: flex; justify-content: space-between; align-items: center;'>
        <div>
            <h4 style='margin: 0; color: #00FFFF;'>🟢 Readiness Score: {prog}%</h4>
            <p style='margin: 5px 0 0 0; color: #FFA500; font-size: 0.9em;'>⚠️ <b>Missing:</b> {missing_text}</p>
        </div>
        <div style='text-align: right;'>
            <p style='margin: 0; color: #888; font-size: 0.8em;'>Recommended Action</p>
            <p style='margin: 0; color: #00FF00; font-weight: bold;'>➡️ Next: {next_action}</p>
        </div>
    </div>
    <br>
    """, unsafe_allow_html=True)

    # --- Upgraded Subway Map (Current / Next / Locked) ---
    st.subheader("🚇 Your Voting Journey")
    steps = st.session_state.steps
    cols = st.columns(len(steps))
    progress_step = int((prog / 100) * len(steps))
    
    for i, step in enumerate(steps):
        with cols[i]:
            if i < progress_step:
                st.markdown(f"<div style='text-align: center; padding: 10px; background-color: #00FF0033; border-radius: 5px; border: 1px solid #00FF00;'>✅<br><b>{step}</b><br><span style='font-size:0.75em; color:#00FF00;'>Completed</span></div>", unsafe_allow_html=True)
            elif i == progress_step:
                # Active Step (You are here)
                st.markdown(f"<div style='text-align: center; padding: 10px; background-color: #FFD70033; border-radius: 5px; border: 1px solid #FFD700;'>📍<br><b style='color: white;'>{step}</b><br><span style='font-size:0.75em; color:#FFD700;'>You are here</span></div>", unsafe_allow_html=True)
            elif i == progress_step + 1:
                # Next Action
                st.markdown(f"<div style='text-align: center; padding: 10px; background-color: #333333; border-radius: 5px; border: 1px dashed #888;'>⏳<br><b style='color: #AAA;'>{step}</b><br><span style='font-size:0.75em; color:#888;'>➡️ Next</span></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='text-align: center; padding: 10px; background-color: #222222; border-radius: 5px; color: #666;'>🔒<br><b>{step}</b></div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)