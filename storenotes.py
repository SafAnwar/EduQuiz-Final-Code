import tkinter as tk
import tkinter.messagebox as messagebox

class NoteTaker:
    def __init__(self, master):
        self.master = master
        master.title("Note Taker")
        master.configure(background='navy')

        self.frame = tk.Frame(master, bg="white")
        self.frame.pack(padx=20, pady=20)

        self.filename_label = tk.Label(self.frame, text="Enter file name:", bg="white", fg="navy", font=("Arial", 12))
        self.filename_label.pack(pady=5)

        self.filename_entry = tk.Entry(self.frame, bg="white", fg="navy", font=("Arial", 10))
        self.filename_entry.pack(pady=5)

        self.label = tk.Label(self.frame, text="Enter your notes:", bg="white", fg="navy", font=("Arial", 12))
        self.label.pack(pady=5)

        self.entry = tk.Text(self.frame, height=10, width=50, bg="white", fg="navy", font=("Arial", 10))
        self.entry.pack(pady=5)

        self.button = tk.Button(self.frame, text="Save Notes", command=self.save_notes, bg="white", fg="navy", font=("Arial", 12))
        self.button.pack(pady=10)

    def save_notes(self):
        filename = self.filename_entry.get().strip()  # Remove leading/trailing whitespace
        if not filename:
            messagebox.showerror("Error", "Please enter a file name.")
            return

        notes = self.entry.get("1.0", "end-1c").strip()  # Remove leading/trailing whitespace
        if not notes:
            messagebox.showerror("Error", "Please enter some notes.")
            return

        try:
            with open(filename + ".txt", "w") as file:
                file.write(notes)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the notes: {str(e)}")
        else:
            messagebox.showinfo("Success", "Notes saved successfully.")
            self.master.destroy()