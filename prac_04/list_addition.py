def add_memberwise(list_1, list_2):
    """add elements in two lists together."""
    if len(list_1) > len(list_2):
        for x in range(len(list_1) - len(list_2)):
            list_2.append(0)
    if len(list_2) > len(list_1):
        for x in range(len(list_2) - len(list_1)):
            list_1.append(0)
    list_3 = [list_1[x] + list_2[x] for x in range(len(list_1))]
    return list_3


numbers = add_memberwise([1, 2, 3], [4, 5, 6])
print(numbers)
