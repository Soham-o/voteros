import streamlit as st

def render_simulator():
    st.markdown("---")
    st.subheader("🧪 Scenario Simulator")
    st.caption("Explore how your choices affect your voting journey")

    # Fetch the active scenario from the session state
    scenario = st.session_state.get("scenario_query", None)

    if not scenario:
        st.info("💡 **Tip:** Ask the Copilot *'What if I forget my ID?'* or *'What if I go at 10 AM?'* to see the consequences here.")
        return

    # A. Missed Registration
    if scenario == "missed_registration":
        st.error("🚨 **Consequence: Voting Blocked**")
        st.markdown("""
        <div style='background-color: #331010; padding: 15px; border-radius: 8px; border-left: 5px solid #FF4B4B;'>
            <h4 style='color: #FF4B4B; margin-top: 0;'>Deadline Missed</h4>
            <p style='color: #DDD; margin-bottom: 5px;'><b>What happens:</b> You will not be allowed to vote.</p>
            <p style='color: #DDD; margin-bottom: 5px;'><b>Why:</b> Your name will not be processed onto the official electoral roll in time.</p>
            <p style='color: #00FFFF; margin-top: 10px; margin-bottom: 0;'>➡️ <b>Next Step:</b> You must wait until the next election cycle. File Form 6 now to prepare for the future.</p>
        </div>
        """, unsafe_allow_html=True)

    # B. Peak Hour Voting
    elif scenario == "peak_hour":
        st.warning("⏱️ **Consequence: Severe Wait Times**")
        st.markdown("""
        <div style='background-color: #332000; padding: 15px; border-radius: 8px; border-left: 5px solid #FFA500;'>
            <h4 style='color: #FFA500; margin-top: 0;'>High Congestion Detected</h4>
            <p style='color: #DDD; margin-bottom: 5px;'><b>What happens:</b> You will face expected wait times of 45-60 minutes.</p>
            <p style='color: #DDD; margin-bottom: 5px;'><b>Why:</b> Going between 9 AM and 11 AM places you in the peak morning rush.</p>
            <p style='color: #00FF00; margin-top: 10px; margin-bottom: 0;'>➡️ <b>Next Step:</b> Shift your visit to the 'Green Zone' (1 PM - 3 PM) for < 15 min wait times.</p>
        </div>
        """, unsafe_allow_html=True)

    # C. No ID
    elif scenario == "no_id":
        st.warning("🪪 **Consequence: Identity Verification Failure**")
        st.markdown("""
        <div style='background-color: #332000; padding: 15px; border-radius: 8px; border-left: 5px solid #FFD700;'>
            <h4 style='color: #FFD700; margin-top: 0;'>Primary ID Missing</h4>
            <p style='color: #DDD; margin-bottom: 5px;'><b>What happens:</b> You risk being turned away from the polling booth.</p>
            <p style='color: #DDD; margin-bottom: 5px;'><b>Why:</b> Without approved ID, your identity and electoral roll status cannot be verified.</p>
            <p style='color: #00FFFF; margin-top: 10px; margin-bottom: 0;'>➡️ <b>Next Step:</b> Bring an alternative approved ID (Aadhaar, Passport, PAN) to the Presiding Officer.</p>
        </div>
        """, unsafe_allow_html=True)

    # D. Relocation
    elif scenario == "relocation":
        st.info("🔀 **Consequence: Alternate Path Triggered**")
        st.markdown("""
        <div style='background-color: #002233; padding: 15px; border-radius: 8px; border-left: 5px solid #00FFFF;'>
            <h4 style='color: #00FFFF; margin-top: 0;'>Constituency Mismatch</h4>
            <p style='color: #DDD; margin-bottom: 5px;'><b>What happens:</b> You cannot vote at your new local booth.</p>
            <p style='color: #DDD; margin-bottom: 5px;'><b>Why:</b> If you relocated without updating, your name remains on the electoral roll at your old address.</p>
            <p style='color: #00FF00; margin-top: 10px; margin-bottom: 0;'>➡️ <b>Next Step:</b> File <b>Form 8</b> immediately to transfer your registration to your current address.</p>
        </div>
        """, unsafe_allow_html=True)