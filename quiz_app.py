import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiple Choice Quiz")

        self.score = 0
        self.current_question_index = 0

        # List of questions, options, and correct answers
        self.questions = [
            {
                'question': "What is the capital of France?",
                'options': ["Berlin", "Madrid", "Paris", "Rome"],
                'correct_answer': 2  # Index of the correct option (Paris)
            },
            {
                'question': "Which planet is known as the Red Planet?",
                'options': ["Earth", "Mars", "Jupiter", "Saturn"],
                'correct_answer': 1  # Index of the correct option (Mars)
            }
        ]

        # Create widgets for displaying questions and options
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=20)

        # Create buttons for the options
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Arial", 12), width=30, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        # Display the first question
        self.display_question()

    def display_question(self):
        """
        Displays the current question and its options on the screen.
        """
        question_data = self.questions[self.current_question_index]
        self.question_label.config(text=question_data['question'])

        for i, option in enumerate(question_data['options']):
            self.option_buttons[i].config(text=option)

    def check_answer(self, selected_option):
        """
        Checks if the selected answer is correct, updates the score, and moves to the next question.
        """
        correct_option = self.questions[self.current_question_index]['correct_answer']
        if selected_option == correct_option:
            self.score += 1

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        """
        Displays the final score and ends the quiz.
        """
        messagebox.showinfo("Quiz Finished", f"Your score: {self.score} out of {len(self.questions)}")
        self.root.quit()

# Create the main window
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
