import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

if GOOGLE_API_KEY is None:
    st.error("API key not found. Please check your .env file.")
else:
    st.success("API key loaded successfully.")
    
# def translate_role_for_streamlit(user_role):
#     if user_role == "model":
#         return "assistant"
#     else:
#         return user_role

# Initialize chat session if not exists
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("Chatbot by rsyd03")

# Input field for user prompt (using st.text_input instead of st.chat_input)
user_prompt = st.text_input("Enter your message")

# Check if user has entered a message and send it
if st.button("Ask"):
    if user_prompt:
        # Display user's message
        # st.chat_message("user").markdown(user_prompt)
        
        # Send message to the model and get response
        gemini_response = st.session_state.chat_session.send_message(user_prompt)
        
        # Display assistant's response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)