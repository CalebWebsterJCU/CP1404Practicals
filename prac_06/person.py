class Person:

    def __init__(self, first_name="John", last_name="Smith", age=0):
        """Initialize the Person class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """Define rules for printing."""
        return f"{self.first_name} {self.last_name}: {self.age}"

    def __repr__(self):
        """Define rules for lists."""
        return f"{self.first_name} {self.last_name}: {self.age}"

    def is_adult(self):
        """Determine if person is under 18 years old."""
        return self.age >= 18


if __name__ == '__main__':
    p1 = Person("Caleb", "Webster", 19)
    print(p1)
    print([p1])
    print(p1.is_adult())
