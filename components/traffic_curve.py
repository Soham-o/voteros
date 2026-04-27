import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def render_traffic():
    st.markdown("---")
    
    # --- Crowd Prediction Chart (matplotlib) ---
    st.subheader("📈 Best Time to Visit Polling Booth")
    
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 3), facecolor='#0E1117')
    ax.set_facecolor('#0E1117')
    
    # Generate bimodal curve (Morning rush, evening rush)
    times = np.linspace(7, 18, 100) 
    crowd = np.sin((times - 7) / 11 * np.pi) * 20 + np.exp(-0.5 * ((times - 9.5)/1.5)**2) * 30 + np.exp(-0.5 * ((times - 16.5)/1.5)**2) * 25 + np.random.normal(0, 1.5, 100)
    crowd = np.clip(crowd, 5, 60)
    
    ax.plot(times, crowd, color='#00FFFF', linewidth=2)
    
    # Highlight Peak (Red) and Best (Green) zones
    ax.fill_between(times, crowd, where=(crowd > 40), color='red', alpha=0.3, label='Peak Hours')
    ax.fill_between(times, crowd, where=(crowd < 20), color='green', alpha=0.3, label='Best Time')
    ax.fill_between(times, crowd, where=((crowd >= 20) & (crowd <= 40)), color='#00FFFF', alpha=0.1)
    
    ax.set_xlabel("Time of Day", color='#888888')
    ax.set_ylabel("Wait Time (Mins)", color='#888888')
    ax.set_xticks([7, 10, 13, 16, 18])
    ax.set_xticklabels(['7 AM', '10 AM', '1 PM', '4 PM', '6 PM'])
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#333')
    ax.spines['bottom'].set_color('#333')
    ax.legend(loc='upper right', frameon=False, labelcolor='#888888')
    
    st.pyplot(fig)
    
    # --- Personalized Recommendation ---
    st.success("✅ **Personalized Recommendation:** Visit between **1 PM – 3 PM**. Historical data shows this is the 'Green Zone' with wait times typically under 15 minutes.")

    st.markdown("---")
    
    # --- EVM Guide ---
    st.subheader("🗳️ Inside the Booth: EVM & VVPAT Guide")
    st.caption("Understand the Electronic Voting Machine process to ensure your vote is counted.")
    
    tab1, tab2, tab3 = st.tabs(["1. The EVM", "2. The Secret Vote", "3. The VVPAT Verification"])
    
    with tab1:
        st.markdown("### The Control Unit & Ballot Unit")
        st.write("When you enter the booth, the Polling Officer will press a button on the **Control Unit** to release a ballot for you.")
        st.info("💡 **Signal:** The green 'Ready' light on your Ballot Unit will turn on.")
        
    with tab2:
        st.markdown("### Casting Your Vote")
        st.write("You will see a list of Candidate Names and Party Symbols on the machine.")
        st.markdown("🔵 **Press the Blue Button** next to your chosen candidate.")
        st.error("Do not press multiple buttons. Only the first press is registered.")
        
    with tab3:
        st.markdown("### The 7-Second Rule (VVPAT)")
        st.write("Next to the EVM is a printer with a glass window (The VVPAT).")
        st.success("1. After you press the blue button, look at the glass window.")
        st.success("2. A paper slip will print showing the Serial Number, Name, and Symbol of your candidate.")
        st.success("3. The slip remains visible for **7 seconds** before falling into the sealed drop box.")
        st.warning("⚠️ If the slip does not match your vote, alert the Presiding Officer immediately!")