import os
import streamlit as st
from dotenv import load_dotenv
from app.chatbot import Chatbot
from app.data_loader import DataLoader
import streamlit as st
from streamlit_chat import message
from config import *
from utils import *

# Load environment variables
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# Check for the presence of the API key
if not openai_api_key:
    raise ValueError("No OpenAI API key found. Please check your environment variables.")

def main():
    # Initialize data loader and chatbot
    st.subheader("Personalized Qigong Assistant")
    
    if 'responses' not in st.session_state:
        st.session_state['responses'] = ["How can I assist you in your Qigong practice?"]

    if 'requests' not in st.session_state:
        st.session_state['requests'] = []
    
    chatbot = Chatbot(openai_api_key)
    chatbot.generate_embeddings()


    # Streamlit UI setup
        
    response_container = st.container()

    request_container = st.container()
    
    
    with request_container:
        request = st.text_input("Query: ", key="input")
    # Handle user query
        if request:
                with st.spinner('Thinking...'):
                    conversation_string = get_conversation_string()
                    response = chatbot.generate_response(request)
                st.session_state.responses.append(response)
                st.session_state.requests.append(request)
    with response_container:
        if st.session_state['responses']:

            for i in range(len(st.session_state['responses'])):
                message(st.session_state['responses'][i],key=str(i))
                if i < len(st.session_state['requests']):
                    message(st.session_state["requests"][i], is_user=True,key=str(i)+ '_user')
                    
                    
if __name__ == "__main__":
    main()


