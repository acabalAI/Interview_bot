import streamlit as st
from agents.question_generator import QuestionGeneratorAgent
from agents.dialogue_manager import DialogueManager
from agents.evaluator import Evaluation
from langchain.chat_models import ChatOpenAI
import os
import streamlit as st
from dotenv import load_dotenv
import streamlit as st
from streamlit_chat import message
from pipeline import interview_pipeline
from utils.config import *

from dotenv import load_dotenv
load_dotenv()

# Initialize AI Client
ai_client = ChatOpenAI(model_name="gpt-3.5-turbo")

def run_chatbot_ui():
    st.title('Interactive Interview Preparation Chatbot')


    # Question Generator Agent Interface
    st.header("Question Generator Agent")
    cv = st.text_area("Enter CV details:")
    job_offer = st.text_area("Enter Job Offer details:")
    generate_questions = st.button("Generate Interview Questions")

    question_generator = QuestionGeneratorAgent(cv, job_offer, ai_client)
    st.session_state.questions = question_generator.generate_questions()

    questions=st.session_state.questions
    
    if st.session_state.questions:
        st.header("Dialogue Manager")
        dialogue_manager = DialogueManager(ai_client, questions)
        if st.button("Conduct Interview"):
            interview_records = dialogue_manager.run_interview()

    # Evaluation Interface
    # Assuming interview_records is stored in session state or generated from Dialogue Manager
    if 'interview_records' in st.session_state and interview_records:
        st.header("Evaluation")
        evaluation_agent = Evaluation(job_offer, ai_client, interview_records)
        if st.button("Generate Evaluation"):
            evaluation = evaluation_agent.generate_evaluation()
            st.json(evaluation)
        
if __name__ == "__main__":
    run_chatbot_ui()