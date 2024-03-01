import tkinter as tk

class StoreInfoOrQuiz:
    def __init__(self):
        self.quiz_option = False
        self.store_option = False
        self.root = tk.Tk()
        self.root.title("Information Storage and Quiz")

        # Set window size and position
        window_width = 300
        window_height = 150
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        self.root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

        # Create label
        self.label = tk.Label(self.root, text="Would you like to store your information or take a quiz?", wraplength=250)
        self.label.pack(pady=10)

        # Create store info button
        self.store_info_btn = tk.Button(self.root, text="Store Info", command=self.store_info, bg='navy', fg='white')
        self.store_info_btn.pack(pady=5, padx=20, ipadx=20, side=tk.LEFT)

        # Create take quiz button
        self.take_quiz_btn = tk.Button(self.root, text="Take Quiz", command=self.take_quiz, bg='navy', fg='white')
        self.take_quiz_btn.pack(pady=5, padx=20, ipadx=20, side=tk.RIGHT)

    def run(self):
        self.root.mainloop()

    def store_info(self):
        print("Storing information...")  # Placeholder for storing information
        self.store_option = True
        self.quiz_option = False
        self.check_and_close()

    def take_quiz(self):
        print("Taking quiz...")  # Placeholder for taking quiz
        self.quiz_option = True
        self.store_option = False
        self.check_and_close()

    def check_and_close(self):
        if self.store_option and self.quiz_option:
            print("Error: Both options selected. Please choose only one.")
        elif not self.store_option and not self.quiz_option:
            print("Error: No option selected. Please choose one.")
        else:
            self.root.destroy()