import tkinter as tk
from tkinter import messagebox


class GoBack:
    def __init__(self):
        try:
            self.option = False
            self.main_menu_window = tk.Tk()
            self.main_menu_window.title("Main Menu")
            self.main_menu_window.configure(bg="navy")

            self.label = tk.Label(self.main_menu_window, text="Do you want to go back to the main menu?", bg="navy", fg="white", font=("Arial", 13))
            self.label.pack(pady=20)

            self.yes_button = tk.Button(self.main_menu_window, text="Yes", command=self.ask_go_back, bg="white", fg="navy", font=("Arial", 12))
            self.yes_button.pack(side="left", padx=20)

            self.no_button = tk.Button(self.main_menu_window, text="No", command=self.close_window, bg="white", fg="navy", font=("Arial", 12))
            self.no_button.pack(side="right", padx=20)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def ask_go_back(self):
        try:
            response = messagebox.askyesno("Go Back", "Are you sure that you would like to go back to the main menu?")
            if response:
                self.option = True
                self.close_window()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def close_window(self):
        try:
            self.main_menu_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def run(self):
        try:
            self.main_menu_window.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")