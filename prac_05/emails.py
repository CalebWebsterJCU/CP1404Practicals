"""
Emails
31/08/2020
This program gets and stores email addresses and names in a dictionary.
"""


def main():
    """Get email and determine name. If user's name is not the determined name, get name. Then add email: name to dict."""
    names_to_emails = {}
    email_address = get_email_address()
    while email_address != '':
        name = determine_name_from_email_address(email_address)
        choice = get_string_in_list(['y', 'n', 'no', 'yes'], f"Is your name {name}? (Y/n) ").lower()
        if choice == 'n' or choice == 'no':
            name = get_nonempty_string("Name: ").title()
        names_to_emails[name] = email_address
        email_address = get_email_address()

    longest_name_length = 0
    for name in names_to_emails:
        if len(name) > longest_name_length:
            longest_name_length = len(name)
    for name in names_to_emails:
        print(f"{name:{longest_name_length}} {names_to_emails.get(name)}")


def get_email_address(prompt: str = "Email Address: ", error: str = "Invalid email address"):
    """Get email address making sure it is valid (includes "@" and ".")"""
    email_address = input(prompt)
    if email_address == '':
        return email_address
    while '@' not in email_address or email_address.count('@') > 1 or '.' not in email_address:
        print(error)
        email_address = input(prompt)
    return email_address


def determine_name_from_email_address(email_address: str):
    """Determine a persons name from their email address."""
    # Find the index of any numbers before the @ symbol
    number_index = 0
    at_symbol_index = email_address.find('@')
    # Find the index of any numbers before the "@" symbol
    for char in email_address[:at_symbol_index]:
        if char.isnumeric():
            number_index = email_address.index(char)
            break
    # The name is any characters before the "@", or before the numbers if any are present
    if number_index:
        name_part = email_address[:number_index]
    else:
        name_part = email_address[:at_symbol_index]
    if '.' in name_part:  # Often names are divided by periods.
        full_name = ''
        names = name_part.split('.')
        for name in names:
            # If name is not the last name, add a space.
            if names.index(name) != len(names) - 1:
                full_name = full_name + name + ' '
            else:
                full_name = full_name + name
    else:
        full_name = name_part
    return full_name.title()


def get_string_in_list(valid_strings, prompt: str = "Input: "):
    """Get a string from the user, making sure it is in a specified list."""
    string = input(prompt)
    while string.lower() not in valid_strings:
        print(f"Invalid input; must be in {valid_strings}")
        string = input(prompt)
    return string


def get_nonempty_string(prompt: str = "String: ", error: str = "Input cannot be blank") :
    """Get a string, making sure it is not blank."""
    string = input(prompt)
    while string == '':
        print(error)
        string = input(prompt)
    return string



main()
