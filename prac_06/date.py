class Date:

    def __init__(self, day, month, year):
        """Initialize the Date class."""
        self.day = day
        self.month = month
        self.year = year
        self.months_to_days = {1: 31, 2: 28, 3: 31,
                               4: 30, 5: 31, 6: 30,
                               7: 31, 8: 31, 9: 30,
                               10: 31, 11: 30, 12: 31}
        if self.is_leap_year():
            self.months_to_days[2] = 29

    def __str__(self):
        """Specify rules for printing class objects."""
        return f"{self.day}/{self.month}/{self.year}"

    def __repr__(self):
        """Specify rules for listing class objects."""
        return f"{self.day}/{self.month}/{self.year}"

    def is_leap_year(self):
        """Determine if a given year is a leap year."""
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    is_leap = True
                else:
                    is_leap = False
            else:
                is_leap = True
        else:
            is_leap = False
        return is_leap

    def add_days(self, number):
        """Add days to date."""
        for x in range(number):
            self.day += 1
            if self.day > self.months_to_days[self.month]:
                self.day = 1
                self.month += 1
                if self.month > 12:
                    self.month = 1
                    self.year += 1


if __name__ == '__main__':
    date1 = Date(1, 1, 2000)
    print(date1)
    print(date1.is_leap_year())
    date1.add_days(100)
    print(f"Expected 10/4/2000, got {date1}")
