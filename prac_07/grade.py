"""
Grade
17/09/2020
This GUI Program takes a users score and displays their grade.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window


def determine_grade(score):
    """Determine grade based on score."""
    if score >= 50:
        return "Pass"
    else:
        return "Fail"


class Grade(App):
    """Construct main app."""
    grade_output_text = StringProperty()

    def build(self):
        """Build the GUI."""
        self.root = Builder.load_file("grade.kv")
        Window.size = (600, 300)
        self.grade_output_text = "Enter Score"
        # self.grade_output = "Enter Score"
        return self.root

    def handle_display_grade(self):
        score = self.get_valid_score()
        grade = determine_grade(score)
        self.grade_output_text = grade
        if grade == "Fail":
            self.root.ids.grade_output.color = (1, 0, 0, 1)
        else:
            self.root.ids.grade_output.color = (0, 1, 0, 1)

    def get_valid_score(self):
        """Get score, returning zero if it is invalid."""
        try:
            score = float(self.root.ids.score_input.text)
            return score
        except ValueError:
            return 0

    def clear_input_output(self):
        """Clear input and output boxes."""
        self.root.ids.score_input.text = ""
        self.grade_output_text = ""


if __name__ == '__main__':
    Grade().run()
