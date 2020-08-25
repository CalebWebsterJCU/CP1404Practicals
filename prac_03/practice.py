import random as r
# Random Things
number = r.randint(0, 1)
if number == 0:
    print(False)
else:
    print(True)

number = r.randint(0, 100)
if number % 2 == 0:
    print(True)
else:
    print(False)

print(r.choice([True, False]))
