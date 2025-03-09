import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    st.error("🚨 API key is missing! Please check your .env file.")

# Initialize session state variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {}
if "tech_stack" not in st.session_state:
    st.session_state.tech_stack = []

# ---- Custom CSS for Better UI ----
st.markdown("""
    <style>
        /* Custom Scrollable Chat History */
        .scrollable-chat {
            max-height: 300px;
            overflow-y: auto;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 10px;
            background-color: #f9f9f9;
        }
        /* Chat Message Styling */
        .user-message {
            background-color: #0078ff;
            color: white;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 5px;
        }
        .bot-message {
            background-color: #ddd;
            color: black;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 5px;
        }
        /* Centered Title */
        .title {
            text-align: center;
            font-size: 28px;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Greeting Message ----
st.markdown("<h1 class='title'>🤖 TalentScout</h1>", unsafe_allow_html=True)
st.write("👋 Welcome! Let's get started with your interview assist process.")

# ---- Candidate Information Collection ----
with st.expander("📋 Candidate Details (Click to Expand)"):
    with st.form("candidate_info_form"):
        st.session_state.candidate_info["Full Name"] = st.text_input("Full Name")
        st.session_state.candidate_info["Email Address"] = st.text_input("Email Address")
        st.session_state.candidate_info["Phone Number"] = st.text_input("Phone Number")
        st.session_state.candidate_info["Years of Experience"] = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)
        st.session_state.candidate_info["Desired Position"] = st.text_input("Desired Position")
        st.session_state.candidate_info["Current Location"] = st.text_input("Current Location")
        tech_stack = st.text_area("Tech Stack (comma-separated, e.g., Python, Django, MySQL)")

        submit_button = st.form_submit_button("🚀 Submit")

if submit_button:
    st.session_state.tech_stack = [tech.strip() for tech in tech_stack.split(",")]
    st.success("✅ Information saved successfully! Let's proceed with technical questions.")

# ---- Generate Technical Questions using Gemini API ----
if st.session_state.tech_stack:
    st.subheader("🎯 Technical Questions")
    for tech in st.session_state.tech_stack:
        with st.spinner(f"Generating questions for {tech}..."):
            response = genai.GenerativeModel("gemini-2.0-flash").generate_content(
                f"Generate 3-5 technical interview questions for {tech}."
            )
            questions = response.text if response else "⚠️ Unable to generate questions."
            st.markdown(f"### {tech} Questions:")
            st.markdown(f"📝 {questions}")

# ---- Chatbot Interaction ----
st.subheader("💬 Chat with the AI Interview Bot")

user_input = st.text_input("Type your message here:")

if user_input:
    if user_input.lower() in ["exit", "quit", "bye"]:
        st.success("🔚 Thank you for your time! We'll get back to you soon.")
        st.session_state.chat_history = []
    else:
        with st.spinner("Thinking... 💭"):
            response = genai.GenerativeModel("gemini-2.0-flash").generate_content(user_input)
            bot_response = response.text if response else "🤖 I'm not sure how to respond to that."
            st.session_state.chat_history.append({"user": user_input, "bot": bot_response})

# ---- Display Chat History ----
if st.session_state.chat_history:
    st.subheader("📜 Chat History")
    st.markdown('<div class="scrollable-chat">', unsafe_allow_html=True)
    
    for chat in st.session_state.chat_history:
        st.markdown(f'<div class="user-message">👤 You: {chat["user"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-message">🤖 Bot: {chat["bot"]}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

