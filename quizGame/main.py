import data
from question_model import Question
from quizBrain import QuizEval

question_bank = []
list_of_questions = data.question_data

for question in list_of_questions:
    question_bank.append(Question(question["text"], question["answer"]))
quiz = QuizEval()
QuizEval.next_question()

