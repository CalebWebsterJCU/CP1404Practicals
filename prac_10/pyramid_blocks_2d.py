"""
Pyramid Blocks
20/10/2020
This program tells it will take to build a 2 dimensional pyramid of height (num of rows) specified by the user.
"""


def main():
    """While input is not blank, display number of blocks needed."""
    num_of_rows = input("Rows: ")
    while num_of_rows != "":
        num_of_rows = int(num_of_rows)
        # blocks_required = calc_blocks_required_1(num_of_rows)
        blocks_required = calc_blocks_required_2(num_of_rows)
        print(f"Blocks required: {blocks_required}")
        num_of_rows = input("Rows: ")
    print("Goodbye")


def calc_blocks_required_1(num_of_rows):
    """Use iteration to calculate the number of blocks required to build a 2d pyramid of a number of rows passed in."""
    blocks_required = 0
    blocks_in_row = 1
    for x in range(num_of_rows):
        blocks_required += blocks_in_row
        blocks_in_row += 1
    return blocks_required


def calc_blocks_required_2(n):
    """Use recursion to calculate the number of blocks required to build a 2d pyramid of a number of rows passed in."""
    if n <= 1:
        return 1
    return calc_blocks_required_2(n - 1) + n


def run_tests():
    """Run tests."""
    assert calc_blocks_required_1(1) == 1
    assert calc_blocks_required_1(2) == 3
    assert calc_blocks_required_1(3) == 6
    assert calc_blocks_required_1(4) == 10
    assert calc_blocks_required_1(5) == 15
    assert calc_blocks_required_2(1) == 1
    assert calc_blocks_required_2(2) == 3
    assert calc_blocks_required_2(3) == 6
    assert calc_blocks_required_2(4) == 10
    assert calc_blocks_required_2(5) == 15


# run_tests()
main()
