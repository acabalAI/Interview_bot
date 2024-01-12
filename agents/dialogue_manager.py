import json
import os
from .base import BaseAgent
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
import pandas as pd
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
import openai
from langchain import PromptTemplate
from langchain.tools import BaseTool
from langchain.chains import LLMChain

from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)

from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

class DialogueManager(BaseAgent):
    def __init__(self, client, questions):
        super().__init__(None, None, client)
        self.questions = questions
        self.interview_records = {}  # Dictionary to store question-answer pairs

    def run_interview(self) -> list[dict[str, str]]:
        for q_dict in self.questions:
            question = q_dict.get('question', '')
            category = q_dict.get('category', '')
            print(f"Interview question: {question} (Category: {category})")

            interview_data = {
                'question': question,
                'category': category,
                'reply': None,
                'followup_questions': []
            }

            # Build the prompt dynamically based on the question
            prompt = ChatPromptTemplate(
                messages=[
                    SystemMessagePromptTemplate.from_template(
                        f"""You are a non-technical interviewer conducting a job interview.
                        You will be discussing with a job applicant exclusively about the question {question}.
                        You are in the middle of the interview, you should continue the flow of the dialogue.
                        If you think the user provides a direct and clear answer, you will just output the sentence "Great, let's continue" and finish the conversation.
                        do not add any content, just limit yourself to discuss the questions provided"""
                    ),
                    MessagesPlaceholder(variable_name="chat_history"),
                    HumanMessagePromptTemplate.from_template("{reply}"),
                ]
            )

            memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

            # Replace ai_client with your AI model

            conversation = LLMChain(prompt=prompt, llm=self.client, memory=memory)

            interviewee_answers = []  # List to store answers for a specific question
            followup_questions = []

            # Conduct the interview with a limit of 3 interactions
            for _ in range(2):
                # Get user input/response
                user_response = input("Applicant's response: ")

                # Store the interviewee's answer
                interviewee_answers.append(user_response)

                # Process user response using the conversation instance
                response = conversation.run({"reply": user_response})
                followup_questions.append(response)

                # Print the AI-generated response or take further actions based on the response
                print(response)

                # Check if the conversation should terminate based on the response
                if "Great, let's continue" in response:
                    break  # End the conversation when the condition is met

            interview_data['reply'] = interviewee_answers[-1] if interviewee_answers else None
            interview_data['followup_questions'] = followup_questions

            # Store the question, reply, and follow-up questions in the interview records
            self.interview_records[question] = interview_data

        return self.interview_records
