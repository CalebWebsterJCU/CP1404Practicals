"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    for i in range(len(subjects)):
        print(subjects[i], "Scores:")
        total = 0
        max_score = 0
        min_score = 100
        number_of_scores = 0
        for score in score_values:
            print(score[i])
            total += score[i]
            number_of_scores += 1
            if score[i] > max_score:
                max_score = score[i]
            if score[i] < min_score:
                min_score = score[i]
        # for score in score_values[i]:
        #     print(score)
        print("Max:", max_score)
        print("Min:", min_score)
        print("Total:", total)
        print("Average:", total / number_of_scores)
        print()
    file_in = open("scores.csv")
    contents = file_in.read()
    file_in.close()
    print(contents)


main()
