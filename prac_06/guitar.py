class Guitar:
    from datetime import datetime
    CURRENT_YEAR = datetime.now().year

    def __init__(self, name="", year=0, cost=0):
        """Initialize Guitar Class."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Define rules for printing."""
        return f"{self.name} ({self.year}): ${self.cost}"

    def __repr__(self):
        """Define rules for lists."""
        return f"{self.name} ({self.year}): ${self.cost}"

    def __lt__(self, other):
        """Define rules for comparing guitars (less than)."""
        return self.year < other.year

    def get_age(self, current_year=CURRENT_YEAR):
        """Calculate the age of the guitar."""
        return current_year - self.year

    def is_vintage(self, current_year=CURRENT_YEAR):
        return self.get_age(current_year) >= 50


if __name__ == '__main__':
    from datetime import datetime
    CURRENT_YEAR = datetime.now().year
    g1 = Guitar("Awesome guitar", 1970, 16000)
    print(g1)
    print([g1])
    print(g1.get_age())
    print(g1.is_vintage())
