try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Denominator cannot be zero!")

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. A ValueError will occur if a string that cannot be converted into an int is entered (eg. "aaa", 1.1)
# 2. A ZeroDivisionError will occur if zero is entered as the denominator
# 3. Yes, by using an if statement before dividing (eg. if denominator != 0:)
