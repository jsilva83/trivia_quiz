import tkinter

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        # Create the user interface.
        self.root_window = tkinter.Tk()
        self.root_window.title('Quizzler')
        # Score label.
        self.score_label = tkinter.Label(self.root_window)
        self.score_label.config(text='Score: 0', pady=20)
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
        self.v_button.config(image=v_button_image, highlightthickness=0, borderwidth=0)
        self.v_button.grid(row=2, column=0, pady=20)
        x_button_image = tkinter.PhotoImage(file='./images/false.png')
        self.x_button = tkinter.Button(self.root_window)
        self.x_button.config(image=x_button_image, highlightthickness=0, borderwidth=0)
        self.x_button.grid(row=2, column=1, pady=20)
        # Wait for events.
        self.root_window.mainloop()
        return
