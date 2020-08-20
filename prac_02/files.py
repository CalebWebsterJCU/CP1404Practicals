# name = input("Name: ").title()
# out_file = open("name.txt", 'w')
# print("Your name is {}".format(name), file=out_file)
# out_file.close()
#
# in_file = open("name.txt", 'r')
# name = in_file.read()[13:].strip()
# print("Your name is {}".format(name))
# in_file.close()

# in_file = open("numbers.txt", 'r')
# num1 = float(in_file.readline())
# num2 = float(in_file.readline())
# in_file.close()
# print("Result is {}".format(num1 + num2))

total = 0
in_file = open("numbers.txt", 'r')
for line in in_file:
    total += float(line)
in_file.close()
print("Total is {}".format(total))

