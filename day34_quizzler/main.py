
import logging as l
l.basicConfig(format='[%(asctime)s.%(msecs)03d] %(message)s', 
              level=l.INFO, 
              datefmt='%I:%M:%S')

from question_model import Question
from question_data import get_question_data_list
from quiz_brain import QuizBrain
from ui import QuizInterface

def get_question_list(q_data_list: list) -> list:
    q_list = []
    for q in q_data_list:
        q_text = q["question"]
        q_answer = q["correct_answer"]
        new_q = Question(q_text, q_answer)
        q_list.append(new_q)
    return q_list


question_data_list = get_question_data_list()

question_list = get_question_list(question_data_list)

quiz = QuizBrain(question_list)

quiz_ui = QuizInterface(quiz)
