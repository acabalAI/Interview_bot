import json
import os
from .base import BaseAgent
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')



class Evaluation(BaseAgent):
    def __init__(self,job_offer, client,interview_records):
          super().__init__(None,job_offer,client)
          self.interview_records=interview_records


          self.template_evaluation_generation = """you are an evaluator of job interview, you will be provided with the job offer {job_offer}
             and the responses given by the user in the interview records {interview_records} that include ('question','followup question','user_reply').
             Your task is based on the information provided :
             Evaluate critically the answers for every category in category ('Personal', 'Role specific', 'Behavioural' and 'Situational'),
            and provide output in the following JSON format based on the adequacy of the responses to the questions and the job offer:
              (
          "Category":
                ("Evaluation": "Critical evaluation of the replies by the user, exclusively based on the user replies",
                "Reason": "Reasons behind the evaluation",
                "Feedback": "Feedback or suggestions for improvement"

               )
        )
            your evaluation should be exclusively based on the replies provided in the interview records and should not include external additions.
            """



          self.prompt_evaluation_generation = PromptTemplate(template=self.template_evaluation_generation, input_variables=["job_offer","interview_records"])

          self.llm_chain_evaluation_generation = LLMChain(prompt=self.prompt_evaluation_generation, llm=self.client)

    def generate_evaluation(self) -> list[dict[str, str]]:
            try:
                evaluation = self.llm_chain_evaluation_generation.run({"job_offer": self.job_offer,"interview_records": self.interview_records})
                parsed_evaluation = json.loads(evaluation)
                return parsed_evaluation

            except Exception as e:
                print(e)
                return " Error generating Evaluation"