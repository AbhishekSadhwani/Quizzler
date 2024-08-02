from tkinter import *
from PIL import ImageTk, Image
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # window
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        # score label
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white",
                                 font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        # canvas
        self.canvas = Canvas(width=300, height=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 150, text="Question goes here",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.get_next_question()
        # buttons
        img = Image.open("images/true.png")
        true_image = ImageTk.PhotoImage(img)
        self.right_button = Button(image=true_image,
                                   bg=THEME_COLOR,
                                   highlightthickness=0,
                                   command=self.is_True)

        self.right_button.grid(row=2, column=0)

        image = Image.open("images/false.png")
        false_image = ImageTk.PhotoImage(image)
        self.wrong_button = Button(image=false_image,
                                   bg=THEME_COLOR,
                                   highlightthickness=0,
                                   command=self.is_false)

        self.wrong_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def is_True(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
