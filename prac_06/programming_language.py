class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialize ProgrammingLanguage class."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if a programming language is dynamic or not."""
        if self.reflection == "Dynamic":
            return True
        else:
            return False
