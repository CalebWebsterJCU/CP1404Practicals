"""
Recursion
21/10/2020
Several recursion exercises
"""


def get_inside_out_string(string, index=0):
    if not len(string) % 2 and index == -round(len(string) / 2) or len(string) % 2 and index == int(len(string) / 2):
        return string[index]
    if index < 0:
        return string[index] + get_inside_out_string(string, -index)
    return string[index] + get_inside_out_string(string, -(index + 1))


def is_palindrome(string, index=0):
    if string[index].lower() == string[-index - 1].lower():
        return True
    if index < 0:
        return True and is_palindrome(string, -index)
    return True and is_palindrome(string, -(index + 1))


print(get_inside_out_string("1234567"))
print(is_palindrome("HannaH"))