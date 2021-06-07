from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=2)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="some question text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=1, columnspan=2, pady=50)

        correct = PhotoImage(file="./images/true.png")
        false = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=correct, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=1, row=2)
        self.false_button = Button(image=false, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=2, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="white")
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the question list\n Your score is {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(3000, self.get_next_question)