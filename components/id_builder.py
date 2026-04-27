import streamlit as st

def render_id_builder():
    st.markdown("---")
    # ------------------------------
    # 1. ECI FORM RECOMMENDER
    # ------------------------------
    st.subheader("📝 Action Required: ECI Forms")
    
    current_form = st.session_state.required_form
    
    if current_form == "Pending...":
        st.info("Chat with VoterOS to determine if you need to file any paperwork.")
    elif current_form == "None! You are registered.":
        st.success(f"**Status:** {current_form}")
    elif "Form 6" in current_form:
        st.error(f"**Required:** {current_form}")
        st.caption("Application for New Voters. Required documents: Age Proof + Address Proof.")
        st.markdown("[🔗 Apply via Voter Portal (NVSP)](#)")
    elif "Form 8" in current_form:
        st.warning(f"**Required:** {current_form}")
        st.caption("Application for Shifting of Residence. You cannot vote at your old booth!")
        st.markdown("[🔗 Apply via Voter Portal (NVSP)](#)")

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------
    # 2. APPROVED ECI DOCUMENTS
    # ------------------------------
    st.subheader("🪪 Approved Polling Booth IDs")
    
    docs = st.session_state.docs
    approved_count = sum(docs.values())
    
    # --- Explicit Consequence & Count Messaging ---
    if approved_count == 0:
        st.warning("⚠️ **Missing Documents:** You currently have NO approved ID selected. **Consequence:** You will not be allowed inside the booth.")
    else:
        st.success(f"✅ **{approved_count} Approved ID(s) Ready:** You only need to bring one physical copy.")
    
    cols = st.columns(3)
    
    for i, (doc, status) in enumerate(docs.items()):
        with cols[i]:
            if status:
                st.markdown(f"<div style='text-align: center; padding: 10px; background-color: #00FF0033; border-radius: 5px; border: 1px solid #00FF00;'>✅<br><b>{doc}</b></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='text-align: center; padding: 10px; background-color: #333333; border-radius: 5px; color: #888;'>❌<br><b>{doc}</b></div>", unsafe_allow_html=True)