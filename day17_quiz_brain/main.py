from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []
for q in question_data:
    q_text = q["question"]
    q_answer = q["correct_answer"]
    new_q = Question(q_text, q_answer)
    question_list.append(new_q)

quiz = QuizBrain(question_list)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
