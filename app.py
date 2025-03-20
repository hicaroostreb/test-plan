from flask import Flask, render_template
import streamlit as st

app = Flask(__name__)


@app.route("/")
def index():
    # Streamlit components
    st.title("AI Agent Builder")
    st.write("Welcome to the AI Agent Builder!")

    # Example input field
    name = st.text_input("Enter your name", "John Doe")
    st.write(f"Hello {name}!")

    # Get the Streamlit components as HTML
    streamlit_components = st.components.v1.html(
        """
        <script>
        const elements = parent.document.querySelectorAll('.stApp');
        elements[0].style.display = 'none';
        </script>
        """,
        height=0,
        width=0,
    )

    return render_template("index.html", streamlit_components=streamlit_components)


if __name__ == "__main__":
    app.run(debug=True)
