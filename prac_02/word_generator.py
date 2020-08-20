"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random as r

MAX_LENGTH = 8
MIN_LENGTH = 3
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

length = r.randint(MIN_LENGTH, MAX_LENGTH)
word_format = ''
for x in range(length):
    word_format += r.choice(['c', 'v'])
# word_format = "ccvcvvc"
# word_format = input("Word Format: ")
word = ""
for kind in word_format:
    if kind == "c":
        word += r.choice(CONSONANTS)
    else:
        word += r.choice(VOWELS)

print(word)
