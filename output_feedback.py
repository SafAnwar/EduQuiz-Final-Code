from tkinter import simpledialog, messagebox
import time
import datetime
import sqlite3

class QuestionFeedback:
    def __init__(self, time_taken, percentage_match, actual_answer, username):
        try:
            self.percentage_match = float(percentage_match)
            if not (0 <= self.percentage_match <= 100):
                raise ValueError("Percentage match must be between 0 and 100")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        self.actual_answer = actual_answer
        try:
            self.time_taken = float(time_taken)
            if self.time_taken < 0:
                raise ValueError("Time taken cannot be negative")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        self.time_taken_formatted = f"{self.time_taken:.2f} seconds"
        self.quiz_date_formatted = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        self.username = username  # Remember the username for storing question history

    def generate_message(self):
        if 90 <= self.percentage_match <= 100:
            return f"Great job! Time taken: {self.time_taken_formatted}. The answer was: {self.actual_answer}"
        elif 80 <= self.percentage_match < 90:
            return f"Almost there! Time taken: {self.time_taken_formatted}. The answer was: {self.actual_answer}"
        elif 75 <= self.percentage_match < 80:
            return f"Not far off! Time taken: {self.time_taken_formatted}. The answer was: {self.actual_answer}"
        else:
            return f"Unlucky! You got it {self.percentage_match:.2f}% correct. Time taken: {self.time_taken_formatted}. The answer was: {self.actual_answer}"

    def display_feedback(self):
        message = self.generate_message()
        messagebox.showinfo("Feedback", message)
        self.store_question_history()  # Store question history after displaying feedback

    def store_question_history(self):
        try:
            conn = sqlite3.connect('userdata.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO question_history (username, question, percentage_match, actual_answer, date_time) VALUES (?, ?, ?, ?, ?)", (self.username, "", self.percentage_match, self.actual_answer, self.quiz_date_formatted))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error storing question history: {e}")
