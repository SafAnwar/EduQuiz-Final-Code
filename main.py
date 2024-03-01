import tkinter as tk
from tkinter import messagebox
import csv
import heapq
import sqlite3

def count_csv_rows(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            row_count = sum(1 for row in reader)
        return row_count
    except FileNotFoundError:
        error_message = "No questions for this topic. Please store questions with the store info option."
        display_error_message(error_message)
        return 0
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        display_error_message(error_message)
        return 0

def display_error_message(message):
  root = tk.Tk()
  root.title("Error")
  root.geometry("400x200")
  root.configure(bg="navy")

  label = tk.Label(root, text=message, fg="white", bg="navy")
  label.pack(pady=10)

  def close_window():
      root.destroy()

  ok_button = tk.Button(root, text="OK", command=close_window)
  ok_button.pack()

  root.mainloop()

def retrieve_question_history(username):
  try:
      conn = sqlite3.connect('userdata.db')
      cursor = conn.cursor()
      cursor.execute("SELECT question, percentage_match, actual_answer FROM question_history WHERE username=?", (username,))
      question_history = {}
      for row in cursor.fetchall():
          question, percentage_match, actual_answer = row
          question_history[question] = {"percentage_match": percentage_match, "actual_answer": actual_answer}
      conn.close()
      return question_history
  except sqlite3.Error as e:
      display_error_message(f"Error retrieving question history: {e}")
      return {}

from welcome_message import WelcomeWindow
welcome_window = WelcomeWindow()
welcome_window.mainloop()

from log_in_or_sign_up import LoginSignup
loginsignup = LoginSignup()
loginsignup.run()

def main(): 
    username = loginsignup.username
    question_history = retrieve_question_history(username)
  
    from storeinfo_or_quiz import StoreInfoOrQuiz
    storeinfoorquiz = StoreInfoOrQuiz()
    storeinfoorquiz.run()

    if storeinfoorquiz.store_option and not storeinfoorquiz.quiz_option:
        from subject_and_topic_selection import SubjectAndTopicSelection
        subjectandtopicselection = SubjectAndTopicSelection()
        subjectandtopicselection.root.mainloop()
        topic = subjectandtopicselection.selected_topic

        from storenotes import NoteTaker
        root = tk.Tk()
        NoteTaker = NoteTaker(root)
        root.mainloop()

        from do_you_want_store_exam_questions import ExamQuestionInquiry
        inquiry = ExamQuestionInquiry()
        inquiry.create_gui()

        store_exam_questions = False
        if inquiry.answer == "Yes":
            store_exam_questions = True
        while store_exam_questions:
            from submit_exam_question_and_answer import SubmitExamQuestionAndAnswer
            root = tk.Tk()
            submit_exam_question_and_answer = SubmitExamQuestionAndAnswer(root, topic)
            from do_you_want_store_exam_questions import ExamQuestionInquiry
            inquiry = ExamQuestionInquiry()
            inquiry.create_gui()
            if inquiry.answer != "Yes":
                store_exam_questions = False

        root.mainloop()

    elif not storeinfoorquiz.store_option and storeinfoorquiz.quiz_option:
        from subject_and_topic_selection import SubjectAndTopicSelection
        subjectandtopicselection = SubjectAndTopicSelection()
        subjectandtopicselection.root.mainloop()
        topic = subjectandtopicselection.selected_topic

        file_path = f"{topic}.csv"
        file_rows = count_csv_rows(file_path)

        for i in range(file_rows):
            from question_displayed import start_quiz
            user_answer, actual_answer, time_taken = start_quiz(topic, i, question_history)

            from answer_checker import AnswerComparison
            answer_comparison = AnswerComparison(user_answer, actual_answer)
            percentage_match = answer_comparison.percentage_match

            from output_feedback import QuestionFeedback
            feedback = QuestionFeedback(username, time_taken, percentage_match, actual_answer)
            feedback.display_feedback()

    from go_back import GoBack
    gobackoption = GoBack()
    gobackoption.run()
    if gobackoption.option:
        main()

#lapceholder

main()
