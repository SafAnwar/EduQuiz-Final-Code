import tkinter as tk

class WelcomeWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome to EduQuiz")
        self.geometry("300x200")

        self.welcome_label = tk.Label(self, text="Welcome to EduQuiz!", font=("Arial", 18), pady=20)
        self.welcome_label.pack()

        self.start_button = tk.Button(self, text="Start EduQuiz", command=self.start_program, bg="navy", fg="white", font=("Arial", 12))
        self.start_button.pack(pady=10)

        self.bind('<Return>', lambda event=None: self.start_program())

        self.start_button.bind('<Button-1>', lambda event: self.close_window())

    def start_program(self):
        try:
            print("EduQuiz program is starting...")
            # Add your main program logic here
        except Exception as e:
            print("An error occurred:", e)
            # Add code to handle the error gracefully

    def close_window(self):
        try:
            self.destroy()
        except Exception as e:
            print("An error occurred while closing the window:", e)
