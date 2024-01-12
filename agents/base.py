import os
#from dotenv import load_dotenv
#load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
from langchain.llms import OpenAI

class BaseAgent:
    """
    Base class for different types of agents in the chatbot application.
    This class provides common attributes and methods that can be inherited by other specific agent classes.
    """

    def __init__(self, cv: str, job_offer: str, client: OpenAI):
        """
        Initialize the base agent with common properties.

        :param cv: The CV text or information.
        :param job_offer: The job offer text or information.
        :param categories: A list of categories for the interview questions.
        :param n_questions: Number of questions to generate or process.
        :param client: The OpenAI client for language model interactions.
        """
        self.cv = cv
        self.job_offer = job_offer
        self.client = client

    