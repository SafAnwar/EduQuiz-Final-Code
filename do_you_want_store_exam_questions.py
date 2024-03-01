import tkinter as tk
# from tkinter import messagebox <------ Before
import tkinter.messagebox as messagebox  # <-------- Now


class ExamQuestionInquiry:
    def __init__(self):
        self.root = tk.Tk()
        self.answer = ""

    def close_window(self):
        self.root.destroy()

    def show_message(self, answer):
        self.answer = answer
        if self.answer.lower() == "yes":
            messagebox.showinfo("Exam Question", "Great! Please prepare your exam question.")
        elif self.answer.lower() == "no":
            messagebox.showinfo("No Exam Question", "No problem. Feel free to submit whenever you do have one.")
        else:
            messagebox.showerror("Error", "Invalid input. Please select 'Yes' or 'No'.")
            return  # Do not close window if input is invalid
        self.close_window()

    def create_gui(self):
        self.root.title("Exam Question Inquiry")
        self.root.configure(background='navy')

        label = tk.Label(self.root, text="Do you have an exam question for the chosen topic?", fg="white", bg="navy", font=("Helvetica", 12))
        label.pack(pady=10)

        yes_button = tk.Button(self.root, text="Yes", width=10, command=lambda: self.show_message("Yes"))
        yes_button.pack(pady=5)

        no_button = tk.Button(self.root, text="No", width=10, command=lambda: self.show_message("No"))
        no_button.pack(pady=5)

        self.root.mainloop()