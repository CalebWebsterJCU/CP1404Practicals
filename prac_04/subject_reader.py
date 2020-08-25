"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_subject_details(data)


def display_subject_details(data: list):
    """Prints details of each subject in a given data set."""
    # Determine longest subject and teacher names, and the largest number of students
    longest_subject_name_length = 0
    longest_teacher_name_length = 0
    largest_number_of_students = 0
    for entry in data:
        if len(entry[0]) > longest_subject_name_length:
            longest_subject_name_length = len(entry[0])
        if len(entry[1]) > longest_teacher_name_length:
            longest_teacher_name_length = len(entry[1])
        if entry[2] > largest_number_of_students:
            largest_number_of_students = entry[2]
    for entry in data:
        # This string is formatted based on the longest names and largest numbers
        print("{0:{5}} is taught by {1:{3}} and has {2:{4}} students".format(entry[0], entry[1], entry[2], longest_teacher_name_length, len(str(largest_number_of_students)), longest_subject_name_length))


def get_data() -> list:
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        data.append(parts)
    input_file.close()
    return data


main()
