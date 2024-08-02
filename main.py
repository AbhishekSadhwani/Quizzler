from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html
from ui import UserInterface

question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"])
    # unescape is used to remove html entities and place original symbols

    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

interface = UserInterface(quiz)


# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
