import streamlit as st

st.title("AI Agent Builder")
st.write("Welcome to the AI Agent Builder!")

# Example input field
name = st.text_input("Enter your name", "John Doe")
st.write(f"Hello {name}!")

# LLM Selection
llm_options = ["Google Gemini", "Hugging Face Interface", "Open Router Interface"]
llm_choice = st.selectbox("Choose your LLM", llm_options)

# API Key Input
api_key = st.text_input(f"Enter your API key for {llm_choice}", type="password")
