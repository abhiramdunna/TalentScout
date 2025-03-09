TALENTSCOUT 
1. INTRODUCTION
1.1 Purpose
The TalentScout is an AI-driven application designed to streamline recruitment by assisting candidates in interview preparation. It collects essential candidate details, generates role-specific technical questions, and facilitates AI-powered interview conversations.
1.2 Scope
This chatbot is designed for use by recruiters, hiring managers, and candidates looking to enhance the interview process. It leverages Google Gemini AI for real-time conversation and question generation.
1.3 Key Features
•	AI-powered interview assistant
•	Candidate information collection
•	Custom technical questions based on the declared tech stack
•	Conversational AI to simulate interviews
•	Secure API integration using .env

 

 
 
 
2. SYSTEM REQUIREMENTS
2.1 Hardware Requirements
Processor:
Minimum Requirement: Intel i3 / AMD Ryzen 3
Recommended Requirement: Intel i5 / AMD Ryzen 5 or higher
RAM:
Minimum Requirement: 4GB
Recommended Requirement: 8GB or higher
Storage:
Minimum Requirement: 2GB free space
Recommended Requirement: SSD recommended
Internet:
Minimum Requirement: Required
Recommended Requirement: High-speed connection
2.2 Software Requirements
Operating System: Windows 10+, macOS, Linux
Python Version: 3.8+
Framework: Streamlit
API: Google Gemini AI
Libraries: Refer to Section 4.2
 
3. INSTALLATION & SETUP
3.1 Cloning the Repository
git clone https://github.com/your-username/talentscout-chatbot.git
cd talentscout-chatbot
3.2 Virtual Environment Setup
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
3.3 Install Dependencies
pip install -r requirements.txt
3.4 Set Up API Key
Create a .env file in the project root.
Add the following line with your Google Gemini API key:
GEMINI_API_KEY=your_google_gemini_api_key_here
3.5 Running the Application
streamlit run app.py
4. SYSTEM DESIGN & ARCHITECTURE
4.1 High-Level Architecture
The chatbot follows a modular design:
Frontend (Streamlit UI) – User interface for interaction
Backend (Python & Gemini AI) – Logic for chat handling and question generation
Database (Session State) – Temporary storage of user responses
4.2 Libraries Used
Library	Purpose
streamlit	UI framework
google-generativeai	Google Gemini API
dotenv	Environment variable handling
os	File & system operations
json	Data formatting
5. FUNCTIONAL SPECIFICATIONS
5.1 User Interface
Home Screen: Introduces the chatbot
Candidate Details Form: Collects user information
Technical Questions: Dynamically generated questions
Chat Window: AI-powered conversation
5.2 Chatbot Flow
Greeting: Welcomes the candidate
Data Collection: Gathers candidate details
Tech Stack Processing: Extracts relevant technologies
Question Generation: Creates technical questions
AI Conversation: Simulates an interview
Exit Handling: Graceful termination
 
6. PROMPT DESIGN STRATEGY
6.1 Candidate Information Prompt
Please provide the following details:
- Full Name
- Email Address
- Phone Number
- Years of Experience
- Desired Position
- Current Location
- Tech Stack (comma-separated)
6.2 Technical Question Generation Prompt
Generate 3-5 technical interview questions for {tech_stack}.
6.3 Conversational Prompts
Follow-up Handling: AI remembers previous responses
Error Handling: Provides meaningful fallback messages
7. CHALLENGES & SOLUTIONS
Challenge	Solution
Google Gemini API key security	Used .env file to store credentials securely
Dynamic question generation	Used Gemini API to generate tailored questions
UI Clutter from Chat History	Implemented scrollable chat window using CSS
Slow responses from AI	Added loading spinner to enhance user experience
8. SECURITY CONSIDERATIONS
Data Privacy: No user data is stored permanently
API Key Protection: .env file ensures security
Session State Handling: Temporary data management
9. FUTURE ENHANCEMENTS
✅ Voice-to-text feature for AI-driven spoken interviews
✅ Resume parsing & analysis for better candidate evaluation
✅ Admin Dashboard to review chat history and candidate performance
10. CONCLUSION
The TalentScout is a powerful AI-driven tool designed to enhance recruitment processes by providing a seamless, automated interview experience. By integrating Google Gemini AI and Streamlit UI, it offers a dynamic and interactive solution for candidates and recruiters alike.
11. REFERENCES
Google Gemini AI: https://ai.google.dev
Streamlit Documentation: https://docs.streamlit.io
Python-dotenv: https://pypi.org/project/python-dotenv/
12. AUTHOR
👨‍💻 Dunna Abhiram
📧 LinkedIn Profile
