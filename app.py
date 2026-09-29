import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# Load .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# Page configuration
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# CSS
st.markdown("""
<style>

/* Entire page */
.stApp {
    background: #0f172a;
}

/* Main content */
.main .block-container {
    max-width: 800px;
    padding-top: 50px;
    padding-bottom: 50px;
}

/* Title */
h1 {
    text-align: center;
    color: #38bdf8 !important;
    font-size: 45px !important;
    font-weight: 700 !important;
}

/* Normal text */
p {
    color: #e2e8f0;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Text area */
.stTextArea textarea {
    background-color: #1e293b !important;
    color: white !important;
    border: 2px solid #334155 !important;
    border-radius: 12px !important;
    padding: 15px !important;
    font-size: 16px !important;
}

/* Text area when clicked */
.stTextArea textarea:focus {
    border: 2px solid #38bdf8 !important;
    box-shadow: 0 0 10px rgba(56, 189, 248, 0.5) !important;
}

/* Generate button */
.stButton > button {
    width: 100% !important;
    height: 50px !important;
    border-radius: 12px !important;
    border: none !important;
    background: linear-gradient(90deg, #2563eb, #7c3aed) !important;
    color: white !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

/* Button hover */
.stButton > button:hover {
    border: none !important;
    transform: scale(1.02);
    box-shadow: 0px 0px 20px rgba(124, 58, 237, 0.6);
}

/* Response */
.response {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 15px;
    padding: 20px;
    margin-top: 20px;
    color: white;
}

/* Response heading */
.response h3 {
    color: #38bdf8;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)


# Title
st.title("🤖 Gemini AI Chatbot")

st.markdown(
    '<div class="subtitle">Ask Gemini anything!</div>',
    unsafe_allow_html=True
)


# Prompt
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words...",
    height=150
)


# Button
if st.button("✨ Generate Response"):

    if prompt.strip():

        with st.spinner("Gemini is thinking..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        st.success("Response generated!")

        st.markdown(
            f"""
            <div class="response">
                <h3>🤖 Gemini Response</h3>
                <p>{response.text}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.warning("Please enter a prompt.")


# Footer
st.markdown(
    '<div class="footer">Powered by Google Gemini • Streamlit</div>',
    unsafe_allow_html=True
)