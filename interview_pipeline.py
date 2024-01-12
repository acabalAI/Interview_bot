from agents.question_generator import QuestionGeneratorAgent
from agents.dialogue_manager import DialogueManager
from agents.evaluator import Evaluation

def interview_pipeline(cv_info, job_offer_info, ai_client):


# Use the ai_client from BaseAgent to activate the question generator
    question_generator = QuestionGeneratorAgent(cv_info, job_offer_info, ai_client)

# Generate questions
    generated_questions = question_generator.generate_questions()
    print(generated_questions)


    interviewer = DialogueManager(ai_client,generated_questions[:5])
    interview_records = interviewer.run_interview()

    print("interview records", interview_records)

    evaluator = Evaluation(job_offer_info, ai_client,interview_records)
    evaluation_result = evaluator.generate_evaluation()

    #print("Generated Questions:")
    #print(generated_questions)
    print("Evaluation Result:")
    print(evaluation_result)
    #return evaluation_result
