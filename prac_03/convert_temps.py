"""This program reads temperatures from a text file and converts them
either from Celsius to Fahrenheit or Fahrenheit to Celsius."""

INPUT_FILE_NAME = 'temps_input.txt'
OUTPUT_FILE_NAME = 'temps_output.txt'


def main():
    """Read temperatures from file and convert them."""
    
    options = ['c', 'f']
    print("Which conversion would you like to perform?\nC)elsius to Fahrenheit\nF)ahrenheit to Celsius")
    # Determine which conversion the user wants to perform.
    selection = input(">>> ").lower()
    while selection not in options:
        print("Invalid option")
        selection = input(">>> ").lower()
        
    file_in = open(INPUT_FILE_NAME, 'r')
    file_out = open(OUTPUT_FILE_NAME, 'w')
    number_of_temps = 0
    for line in file_in:
        try:
            temp = float(line.strip())
            # Convert temperature using the user's selection.
            if selection == options[0]:
                converted_temp = celsius_to_fahrenheit(temp)
            else:
                converted_temp = fahrenheit_to_celsius(temp)
            print(converted_temp, file=file_out)
            number_of_temps += 1
        # Catch value error, such as a string, in the temps.
        except ValueError:
            print("ERROR: Please check input data")
    print("Successfully wrote {0} converted temperatures to '{1}'".format(number_of_temps, OUTPUT_FILE_NAME))

    file_out.close()
    file_in.close()


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return 5 / 9 * (fahrenheit - 32)


main()
