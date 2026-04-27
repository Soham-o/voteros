import streamlit as st
from components.chat_interface import render_chat
from components.visual_timeline import render_timeline
from components.id_builder import render_id_builder
from components.traffic_curve import render_traffic
from utils.state_manager import init_state
from components.scenario_simulator import render_simulator

st.set_page_config(layout="wide", page_title="VoterOS", page_icon="🗳️")

# Load CSS
with open("assets/custom_styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize state
init_state()

# Layout
left, right = st.columns([1, 2])

with left:
    render_chat()

with right:
    st.title("📊 Civic Journey Engine")

    render_timeline()
    render_simulator()   
    render_id_builder()
    render_traffic()