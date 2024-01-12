import json
import os
from .base import BaseAgent
#from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

class QuestionGeneratorAgent(BaseAgent):
    def __init__(self, cv, job_offer,client):
        super().__init__(cv, job_offer, client)
        """
        Initializes the QuestionGeneratorAgent with the same parameters as BaseAgent.
        """
        self.cv = cv
        self.job_offer = job_offer
        self.client = client
        
        self.template_question_generation = """
        you are an non-technical interviewer conducting a job interview.
        You will be provided with the cv {cv} and the job offer {job_offer}
        and will generate one question for each of the 4 following categories ('Personal', 'Role specific', 'Behavioural' and 'Situational'), only the number specified as number of questions.
        You should take into consideration the cv and the job offer to generate valid and valuable questions across all the categories.
        You answer strictly as single JSON string. Don't include any other verbose texts and don't include the markdown syntax anywhere.JSON format: ["question":, "category":].
        """

        self.prompt_question_generation = PromptTemplate(template=self.template_question_generation, 
                                                         input_variables=["cv", "job_offer"])
        self.llm_chain_question_generation = LLMChain(prompt=self.prompt_question_generation, llm=self.client)

    def generate_questions(self) -> list[dict[str, str]]:
        """
        Generates interview questions based on the provided CV, job offer
        :return: A list of questions in the format [{question: str, category: str}].
        """
        try:
            generated_questions_json = self.llm_chain_question_generation.run({
                'cv': self.cv,
                "job_offer": self.job_offer
            }
            )
            questions_parsed = json.loads(generated_questions_json)
            return questions_parsed
        except Exception as e:
            print(f"Error generating questions: {e}")
            return []

