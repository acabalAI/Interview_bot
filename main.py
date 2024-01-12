from dotenv import load_dotenv
import os
load_dotenv()

from pipeline.interview_pipeline import interview_pipeline
from utils import *

# Load environment variables from .env file
load_dotenv()

# Application Title
APP_TITLE = "Interview Simulator"

# OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY in your environment.")


cv="With extensive expertise spanning talent acquisition, employee relations, and HR operations, I am a seasoned HR Specialist with a track record of success. Armed with a rich background of [X years] in the field, I specialize in crafting and implementing robust HR strategies aimed at attracting top-tier talent, bolstering retention rates, and nurturing a thriving work culture. My forte lies in streamlining HR processes, optimizing efficiency, and fostering career growth among employees. Noteworthy achievements include orchestrating recruitment initiatives that elevated candidate quality by 30%, alongside spearheading engagement programs that yielded a remarkable 20% improvement in retention rates. My educational background includes an MBA and a BSc in Human Resources Management, complemented by certifications such as the SHRM Certified Professional (SHRM-CP) and other relevant credentials. My skill set encompasses talent acquisition, performance management, HRIS administration, policy development, and effective communication, making me a valuable asset adept at navigating the dynamic landscape of human resources."
job_offer="Seeking a vibrant addition to our team, is on the lookout for a seasoned Human Resources Specialist. This pivotal role involves driving talent acquisition, nurturing employee relations, and optimizing HR operations to bolster our company's growth trajectory. We prioritize fostering a positive workplace culture and innovation across all facets of our operations. The ideal candidate will spearhead recruitment strategies, implement engaging employee programs, manage performance appraisals, and streamline HR processes. A Bachelor's degree in Human Resources Management or a related field, coupled with [X years] of HR experience, is required, with expertise in HRIS systems, talent sourcing tools, and strong communication skills. Certifications like SHRM-CP or PHR would be advantageous. We offer competitive compensation, comprehensive benefits, and a supportive work environment that champions professional development. Join us in shaping an environment where talent thrives and success blossoms"
from langchain.chat_models import ChatOpenAI

ai_client = ChatOpenAI(model_name="gpt-3.5-turbo")

def main():
    evaluation=interview_pipeline(cv, job_offer,ai_client)
    print(evaluation)

if __name__ == "__main__":
    main()