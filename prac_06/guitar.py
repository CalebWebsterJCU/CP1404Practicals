class Guitar:

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

    def get_age(self, current_year):
        """Calculate the age of the guitar."""
        age = current_year - self.year
        return age

    def is_vintage(self, this_year):
        age = self.get_age(this_year)
        if age >= 50:
            return True
        else:
            return False


if __name__ == '__main__':
    from datetime import datetime
    CURRENT_YEAR = datetime.now().year
    g1 = Guitar("Awesome guitar", 1970, 16000)
    print(g1)
    print([g1])
    print(g1.get_age(CURRENT_YEAR))
    print(g1.is_vintage(CURRENT_YEAR))
