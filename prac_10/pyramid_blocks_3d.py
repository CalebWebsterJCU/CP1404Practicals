"""
Pyramid Blocks 3D
20/10/2020
This program tells it will take to build a 3 dimensional pyramid of height (num of layers) specified by the user.
"""


def main():
    """While input is not blank, display number of blocks needed."""
    num_of_layers = input("Layers: ")
    while num_of_layers != "":
        num_of_layers = int(num_of_layers)
        # blocks_required = calc_blocks_required_1(num_of_layers)
        blocks_required = calc_blocks_required_2(num_of_layers)
        print(f"Blocks required: {blocks_required}")
        num_of_layers = input("Layers: ")
    print("Goodbye")


def calc_blocks_required_1(num_of_layers):
    """Use iteration to calculate the number of blocks required to build a 3D pyramid of a number of layers passed in."""
    blocks_required = 0
    layer_width = 2
    for x in range(num_of_layers):
        blocks_required += layer_width ** 2
        layer_width += 2
    return blocks_required


def calc_blocks_required_2(n):
    """Use recursion to calculate the number of blocks required to build a 3D pyramid of a number of layers passed in."""
    blocks_to_add = (n * 2) ** 2
    if n <= 1:
        return 4
    return calc_blocks_required_2(n - 1) + blocks_to_add


def run_tests():
    """Run tests."""
    assert calc_blocks_required_2(2) == 20
    assert calc_blocks_required_2(3) == 56
    assert calc_blocks_required_1(4) == 120
    assert calc_blocks_required_1(5) == 220


run_tests()
# main()
