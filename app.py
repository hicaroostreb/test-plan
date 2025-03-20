import streamlit as st

st.title("AI Agent Builder")
st.write("Welcome to the AI Agent Builder!")

# LLM Selection
llm_options = ["Google Gemini", "Hugging Face Interface", "Open Router Interface"]
llm_choice = st.selectbox("Choose your LLM", llm_options)

# API Key Input
api_key = st.text_input(f"Enter your API key for {llm_choice}", type="password")

if st.button("Confirm and Store Information"):
    st.write(f"LLM Choice: {llm_choice}")
    st.write("API key stored securely.")
    # In a real application, you would store this information securely
