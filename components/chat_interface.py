import streamlit as st
# --- NEW: Import both functions ---
from utils.llm_logic import process_input, get_gemini_response

def render_chat():
    st.header("💬 VoterOS Copilot")
    st.caption("⚡ Powered by Gemini-ready architecture (Google Vertex AI)")
    st.markdown("---")

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    user_input = st.chat_input("Ask about voting...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # --- NEW: Hybrid Intelligence Pipeline ---
        # 1. Run local rules to update UI state and get current context
        system_context = process_input(user_input)
        
        # 2. Pass context to Gemini to generate conversational UI response
        response = get_gemini_response(user_input, system_context)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()