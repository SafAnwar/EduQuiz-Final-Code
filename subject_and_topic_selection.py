import tkinter as tk
from tkinter import ttk

class SubjectAndTopicSelection:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Note Taking App")
        self.root.configure(bg='navy')

        self.mainframe = ttk.Frame(self.root, padding="20")
        self.mainframe.grid(column=0, row=0, sticky=(tk.W, tk.N, tk.E, tk.S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        self.subjects = ['Biology', 'Chemistry', 'Mathematics', 'Computer Science', 'Physics']

        self.subject_label = ttk.Label(self.mainframe, text="Select Subject:", background='navy', foreground='white')
        self.subject_label.grid(column=0, row=0, sticky=tk.W)

        self.subject_combobox = ttk.Combobox(self.mainframe, values=self.subjects, state="readonly", width=40)
        self.subject_combobox.grid(column=1, row=0, padx=10, pady=10)
        self.subject_combobox.current(0)

        self.biology_topics = ['Biological Molecules', 'Cells', 'Exchange of Substances', 'Genetics, Biodiversity and Classification', 'Energy Transfer In and Between Organisms', 'Responding to Changes in Environment', 'Genetics, Populations, Evolution and Ecosystems', 'Control of Gene Expression']

        self.chemistry_topics = ['Physical I', 'Physical II', 'Inorganic I', 'Inorganic II', 'Organic I', 'Organic II']

        self.physics_topics = ['Measurements and Errors', 'Particles and Radiation', 'Waves', 'Mechanics and Materials', 'Electricity', 'Further Mechanics', 'Thermal Physics', 'Fields and Their Consequences', 'Nuclear Physics']

        self.mathematics_topics = ['Proof', 'Algebra and Functions', 'Coordinate Geometry', 'Sequences and Series', 'Trigonometry', 'Exponentials and Logarithms', 'Differentiation', 'Integration', 'Numerical Methods', 'Vectors', 'Sampling', 'Data Presentation and Interpretation', 'Probability', 'Statistical Distributions', 'Hypothesis Testing', 'Quantities and Units in Mechanics', 'Kinematics', "Forces and Newton's Laws", 'Moments']

        self.computer_science_topics = ['Fundamentals of Programming', 'Fundamentals of Data Structures', 'Fundamentals of Algorithms', 'Theory of Computation', 'Fundamentals of Data Representation', 'Fundamentals of Computer Systems', 'Fundamentals of Computer Organisation and Architecture', 'Consequences of Uses of Computing', 'Fundamentals of Communication and Networking', 'Fundamentals of Databases', 'Big Data', 'Fundamentals of Functional Programming', 'Systematic Approach to Problem Solving']

        self.topic_dict = {'Biology': self.biology_topics, 'Chemistry': self.chemistry_topics, 'Physics': self.physics_topics, 'Mathematics': self.mathematics_topics, 'Computer Science': self.computer_science_topics}

        self.topic_label = ttk.Label(self.mainframe, text="Select Topic:", background='navy', foreground='white')
        self.topic_label.grid(column=0, row=1, sticky=tk.W)

        self.selected_subject = self.subjects[0]
        self.selected_topics = self.topic_dict[self.selected_subject]

        self.topic_combobox = ttk.Combobox(self.mainframe, values=self.selected_topics, state="readonly", width=40)
        self.topic_combobox.grid(column=1, row=1, padx=10, pady=10)
        self.topic_combobox.current(0)

        self.subject_combobox.bind("<<ComboboxSelected>>", lambda event: self.update_topics())

        self.submit_button = ttk.Button(self.mainframe, text="Submit", command=self.get_selection)
        self.submit_button.grid(column=0, row=2, columnspan=2, pady=10)

        self.selected_topic = None  # Initialize selected_topic attribute

    def update_topics(self):
        selected_subject = self.subject_combobox.get()
        selected_topics = self.topic_dict.get(selected_subject, [])
        self.topic_combobox['values'] = selected_topics
        if selected_topics:
            self.topic_combobox.current(0)
        else:
            self.topic_combobox.set('')

    def get_selection(self):
        subject = self.subject_combobox.get()
        selected_topic = self.topic_combobox.get()
        if subject and selected_topic:
            self.selected_topic = selected_topic
            print("Subject:", subject)
            print("Topic:", self.selected_topic)
            self.close_window()
        else:
            print("Please select both a subject and a topic.")

    def close_window(self):
        self.root.destroy()