"""
Grade
17/09/2020
This GUI Program takes a users score and displays their grade.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window


def determine_jcu_grade(score):
    """Determine JCU Grade based on score input."""
    if score < 50:
        return "Fail"
    elif score < 64:
        return "Pass"
    elif score < 74:
        return "Credit"
    elif score < 84:
        return "Distinction"
    else:
        return "High Distinction"


class Grade(App):
    """Construct main app."""
    grade_output_text = StringProperty()

    def build(self):
        """Build the GUI."""
        self.root = Builder.load_file("grade.kv")
        Window.size = (600, 300)
        self.grade_output_text = "Enter Score"
        return self.root

    def handle_display_grade(self):
        """Display grade based on score input."""
        score, is_valid = self.get_score()
        if is_valid:
            grade = determine_jcu_grade(score)
            self.grade_output_text = grade
            if grade == "Fail":
                self.root.ids.grade_output.color = (1, 0, 0, 1)
            else:
                self.root.ids.grade_output.color = (0, 1, 0, 1)
        else:
            self.grade_output_text = "Invalid Score"
            self.root.ids.grade_output.color = (1, 1, 1, 1)

    def get_score(self):
        """Get score, returning zero if it is invalid."""
        is_valid = False
        score = self.root.ids.score_input.text
        try:
            score = float(score)
            if 100 >= score >= 0:
                is_valid = True
        except ValueError:
            pass
        return score, is_valid

    def clear_input_output(self):
        """Clear input and output boxes."""
        self.root.ids.score_input.text = ""
        self.grade_output_text = ""


if __name__ == '__main__':
    Grade().run()
