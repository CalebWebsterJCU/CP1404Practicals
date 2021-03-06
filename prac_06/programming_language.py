class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialize ProgrammingLanguage class."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return printing instructions."""
        return f"{self.name}, {self.typing}, typing, Reflection={self.reflection}, First appeared in {self.year}"

    def __repr__(self):
        return f"{self.name}, {self.typing}, typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check if a programming language is dynamic or not."""
        return self.typing == "Dynamic"
