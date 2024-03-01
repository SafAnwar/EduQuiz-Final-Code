import tkinter as tk
from tkinter import ttk
import csv
import time

class QuestionDisplayed:
    def __init__(self, master, topic, file_rows, question_history):
        self.topic = topic
        self.master = master
        self.master.title("Quiz")
        self.file_rows = file_rows
        self.master.configure(bg='navy')
        self.user_answer = None
        self.actual_answer = None
        self.question_history = question_history

        try:
            self.load_question()
        except Exception as e:
            self.display_error_message(str(e))
            return

        self.create_widgets()

    def load_question(self):
        try:
            if self.question_history:
                # Retrieve questions based on historical performance using a priority queue
                priority_queue = []
                for question, answer in self.question_history.items():
                    heapq.heappush(priority_queue, (answer["percentage_match"], question))

                # Get the question with the lowest percentage match (poorest performance)
                _, selected_question = heapq.heappop(priority_queue)
                self.question = selected_question
                self.actual_answer = self.question_history[selected_question]["actual_answer"]
            else:
                with open(f'{self.topic}.csv', 'r') as file:
                    reader = csv.reader(file)
                    rows = list(reader)
                    if len(rows) <= self.file_rows:
                        raise ValueError("Invalid file_rows value. Please provide a valid row number.")
                    if len(rows[self.file_rows]) < 2:
                        raise ValueError("Invalid CSV format. Each row should contain at least 2 columns.")
                    self.question = rows[self.file_rows][0]  # Assuming the first column contains the questions
                    self.actual_answer = rows[self.file_rows][1]
        except FileNotFoundError:
            raise FileNotFoundError(f"No questions for this topic. Please store questions with the store info option")
        except IndexError:
            raise IndexError("Invalid CSV format. Make sure each row contains at least two columns.")

    def display_error_message(self, message):
        error_label = ttk.Label(self.master, text=message, background='navy', foreground='red', font=('Arial', 12))
        error_label.pack(pady=20)

    def submit_answer(self):
        self.user_answer = self.answer_entry.get()
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time
        self.master.destroy()

    def create_widgets(self):
        self.question_label = ttk.Label(self.master, text=self.question, background='navy', foreground='white', font=('Arial', 14))
        self.question_label.pack(pady=20)

        self.answer_entry = ttk.Entry(self.master, width=30)
        self.answer_entry.pack(pady=10)

        self.submit_button = ttk.Button(self.master, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=10)

def start_quiz(topic, file_rows, question_history):
    root = tk.Tk()
    try:
        app = QuestionDisplayed(root, topic, file_rows, question_history)
    except Exception as e:
        root.destroy()
        raise e
    root.mainloop()
    return app.user_answer, app.actual_answer, app.time_taken
