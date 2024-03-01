import sqlite3
import tkinter as tk
from tkinter import simpledialog, messagebox
import datetime
import hashlib  # Import hashlib for hashing passwords

class LoginSignup:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('userdata.db')
            self.cursor = self.conn.cursor()
            self.create_table()
            self.create_question_history_table()  # Add this line to create question history table
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {e}")
            self.conn = None

    def create_table(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                                (username TEXT PRIMARY KEY, password TEXT)''')
            self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error creating table: {e}")

    def create_question_history_table(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS question_history
                                (username TEXT, question TEXT, percentage_match REAL, actual_answer TEXT, date_time TEXT)''')
            self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error creating question history table: {e}")

    def hash_password(self, password):
        # Hash the password using SHA-256
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self):
        if not self.conn:
            messagebox.showerror("Database Error", "Database connection is not established")
            return

        try:
            username = simpledialog.askstring("Login", "Enter your username:")
            password = simpledialog.askstring("Login", "Enter your password:")

            hashed_password = self.hash_password(password)  # Hash the provided password

            self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
            if self.cursor.fetchone() is not None:
                messagebox.showinfo("Login Successful", f"Welcome, {username}!")
                self.root.destroy()  # Close the window after successful login
                self.username = username  # Remember username for question history
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error executing login query: {e}")

    def signup(self):
        if not self.conn:
            messagebox.showerror("Database Error", "Database connection is not established")
            return

        try:
            username = simpledialog.askstring("Sign Up", "Enter a username:")
            password = simpledialog.askstring("Sign Up", "Enter a password:")

            hashed_password = self.hash_password(password)  # Hash the provided password

            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            self.conn.commit()
            messagebox.showinfo("Sign Up Successful", f"Welcome, {username}! You have successfully signed up.")
            self.root.destroy()  # Close the window after successful signup
            self.username = username
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error executing signup query: {e}")

    def run(self):
        self.root = tk.Tk()
        self.root.title("Login System")

        label = tk.Label(self.root, text="Log in or sign up to your free EduQuiz account", font=("Helvetica", 10))
        label.pack(pady=10)

        login_button = tk.Button(self.root, text="Login", command=self.login)
        login_button.pack(pady=5)

        signup_button = tk.Button(self.root, text="Sign Up", command=self.signup)
        signup_button.pack(pady=5)

        self.root.mainloop()

    def __del__(self):
        if self.conn:
            self.conn.close()

    def insert_question_history(self, question, percentage_match, actual_answer, date_time):
        try:
            self.cursor.execute("INSERT INTO question_history (username, question, percentage_match, actual_answer, date_time) VALUES (?, ?, ?, ?, ?)", (self.username, question, percentage_match, actual_answer, date_time))
            self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error inserting question history: {e}")