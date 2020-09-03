"""
Hex Colours
31/08/2020
This program shows different colour names and their hexidecimal codes.
Data Retrieved from https://www.color-hex.com/color-names.html.
"""

FILE_NAME = "colour_hex_values.txt"

name_to_hex = {}
file_in = open(FILE_NAME, 'r')
for line in file_in:
    colour_name, colour_hex = line.strip().split(" ")
    name_to_hex[colour_name] = colour_hex
file_in.close()

name = input("Colour Name: ")
while name != "":
    try:
        print(f"The hex value for {name} is {name_to_hex[name]}")
    except KeyError:
        print("Invalid input")
    name = input("Colour Name: ")
print("Goodbye!")
