"""This program writes random temperatures to a text file."""

import random as r

MINIMUM_TEMPERATURE = -200
MAXIMUM_TEMPERATURE = 200
FILE_NAME = 'temps_input.txt'
NUMBER_OF_SCORES = 25

file_out = open(FILE_NAME, 'w')
for x in range(NUMBER_OF_SCORES):
    score = r.randint(MINIMUM_TEMPERATURE, MAXIMUM_TEMPERATURE)
    print(score, file=file_out)
file_out.close()
