import streamlit as st

st.title("AI Agent Builder")
st.write("Welcome to the AI Agent Builder!")

# LLM Selection
if "llm_choice" not in st.session_state:
    st.session_state.llm_choice = "Google Gemini"

col1, col2, col3 = st.columns(3)

with col1:
    st.image("icons/gemini.webp", width=100)
    if st.button("Google Gemini"):
        st.session_state.llm_choice = "Google Gemini"

with col2:
    st.image("icons/huggingface.png", width=100)
    if st.button("Hugging Face Interface"):
        st.session_state.llm_choice = "Hugging Face Interface"

with col3:
    st.image("icons/openrouterai.png", width=100)
    if st.button("Open Router Interface"):
        st.session_state.llm_choice = "Open Router Interface"

llm_choice = st.session_state.llm_choice

# API Key Input
api_key = st.text_input(f"Enter your API key for {llm_choice}", type="password")

if st.button("Confirm and Store Information"):
    st.write(f"LLM Choice: {llm_choice}")
    st.write("API key stored securely.")
    # In a real application, you would store this information securely
