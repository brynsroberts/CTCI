"""
reference: https://www.youtube.com/watch?v=rf6uf3jNjbo
"""

def towers_of_hanoi(n, start, end):
    # base case
    if n == 1:
        print_move(start, end)

    # recursive call
    else:
        other = 6 - (start + end)
        towers_of_hanoi(n - 1, start, other)
        print_move(start, end)
        towers_of_hanoi(n - 1, other, end)


def print_move(start, end):
    print(f'{start} -> {end}')


n = 2
towers_of_hanoi(20, 1, 3)
