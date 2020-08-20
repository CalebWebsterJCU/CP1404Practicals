"""
Menu Program
This program functions as a simple menu and allows the user to
enter his/her name and select "Hello" or "Goodbye".
"""

MENU = """(H)ello
(G)oodbye
(Q)uit
"""


def main():
    """Get user's name and print greeting or farewell based on user's choice."""
    name = input("Enter name: ").title()
    print(MENU)
    selection = input(">>> ").lower()
    while selection != 'q':
        if selection == 'h':
            print("Hello", name)
        elif selection == 'g':
            print("Goodbye", name)
        else:
            print("Invalid choice")
        print(MENU)
        selection = input(">>> ").lower()
    print("finished.")


main()
