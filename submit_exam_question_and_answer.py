import tkinter as tk
from tkinter import messagebox
import csv

class SubmitExamQuestionAndAnswer:
    def __init__(self, master, topic):
        self.master = master
        master.title("Add Exam Question")
        master.configure(bg="navy")
        self.topic = topic

        self.question_label = tk.Label(master, text="Question:", bg="navy", fg="white")
        self.question_label.grid(row=1, column=0, padx=10, pady=10)
        self.question_entry = tk.Entry(master)
        self.question_entry.grid(row=1, column=1, padx=10, pady=10)

        self.answer_label = tk.Label(master, text="Answer:", bg="navy", fg="white")
        self.answer_label.grid(row=2, column=0, padx=10, pady=10)
        self.answer_entry = tk.Entry(master)
        self.answer_entry.grid(row=2, column=1, padx=10, pady=10)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_question, bg="white", fg="navy")
        self.submit_button.grid(row=3, columnspan=2, padx=10, pady=10)

    def submit_question(self):
        question = self.question_entry.get()
        answer = self.answer_entry.get()

        # Check if both fields are not empty
        if not question.strip() or not answer.strip():
            messagebox.showerror("Error", "Please enter both question and answer.")
            return

        # Replace commas in question and answer with a different character
        question = question.replace(',', ';')
        answer = answer.replace(',', ';')

        # Check if the question already exists in the CSV file
        if self.question_exists(question):
            messagebox.showerror("Error", "This question already exists in the database.")
            return

        try:
            with open(f"{self.topic}.csv", "a", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([question.title(), answer.title()])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return

        messagebox.showinfo("Success", "Question submitted successfully!")
        self.master.destroy()

    def question_exists(self, question):
        try:
            with open(f"{self.topic}.csv", "r", newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row[0] == question.title():
                        return True
        except FileNotFoundError:
            return False
        return False