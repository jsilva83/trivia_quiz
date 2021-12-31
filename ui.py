import tkinter
import quiz_brain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, a_quiz_brain: quiz_brain.QuizBrain) -> None:
        # Hold on to the quiz object.
        self.quiz = a_quiz_brain
        # Create the user interface.
        self.root_window = tkinter.Tk()
        self.root_window.title('Quizzler')
        self.root_window.config(bg=THEME_COLOR)
        # Score label.
        self.score_label = tkinter.Label(self.root_window)
        self.score_label.config(text='Score: 0', fg='white', bg=THEME_COLOR, pady=20)
        self.score_label.grid(row=0, column=1)
        # Canvas to display text.
        self.question_canvas = tkinter.Canvas(self.root_window)
        self.question_canvas.config(width=300, height=250, bg='white')
        self.question_text = self.question_canvas.create_text(150, 125,
                                                              text='question text here',
                                                              width=270,
                                                              font=('arial', 20, 'italic'),
                                                              fill='black'
                                                              )
        self.question_canvas.grid(row=1, column=0, columnspan=2, padx=20)
        # Create buttons.
        v_button_image = tkinter.PhotoImage(file='./images/true.png')
        self.v_button = tkinter.Button(self.root_window)
        self.v_button.config(image=v_button_image, highlightthickness=0,
                             borderwidth=0, command=self.true_button_pressed)
        self.v_button.grid(row=2, column=0, pady=20)
        x_button_image = tkinter.PhotoImage(file='./images/false.png')
        self.x_button = tkinter.Button(self.root_window)
        self.x_button.config(image=x_button_image, highlightthickness=0,
                             borderwidth=0, command=self.false_button_pressed)
        self.x_button.grid(row=2, column=1, pady=20)
        # Initialize with a first question.
        self.get_next_question()
        # Wait for events.
        self.root_window.mainloop()
        return

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text='Reached the end of the quiz!')
            self.v_button.config(state='disabled')
            self.x_button.config(state='disabled')
        return

    def true_button_pressed(self):
        is_correct = self.quiz.check_answer('True')
        self.give_feedback(is_correct)
        return

    def false_button_pressed(self):
        is_correct = self.quiz.check_answer('False')
        self.give_feedback(is_correct)
        return

    def give_feedback(self, in_answer: bool):
        if in_answer:
            self.question_canvas.config(bg='green')
            self.question_canvas.itemconfig(self.question_text, fill='white')
        else:
            self.question_canvas.config(bg='red')
            self.question_canvas.itemconfig(self.question_text, fill='white')
        self.root_window.after(2000, self.reset_canvas)
        return

    def reset_canvas(self):
        self.question_canvas.config(bg='white')
        self.question_canvas.itemconfig(self.question_text, fill='black')
        self.get_next_question()
        return
