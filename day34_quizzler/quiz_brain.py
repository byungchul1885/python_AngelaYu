import logging as l
import html
from question_model import Question

class QuizBrain:

    def __init__(self, q_list: list[Question]):
        l.info(f"class QuizBrain: __init__")
        
        self.q_number = 0
        self.score = 0
        self.q_list = q_list
        self.curr_q : Question = None

    def still_has_questions(self) -> bool:
        return self.q_number < len(self.q_list)

    def next_question(self) -> str:
        self.curr_q = self.q_list[self.q_number]
        self.q_number += 1
        q_text = html.unescape(self.curr_q.text)
        return f"Q.{self.q_number}: {q_text}"

    def check_answer(self, user_answer: str) -> bool:
        correct_answer = self.curr_q.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

