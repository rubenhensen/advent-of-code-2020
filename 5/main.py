import re

parse_regex = re.compile("^(?P<rows>[BF]*)(?P<columns>[LR]*)")

filename = '5/input.txt'
taken_seats = set()

def parse_input(line):
        (row, column) = parse_regex.search(line).groups()
        return (row, column)

def read_file():
    with open(filename) as file:
        return file.readlines()

def binary_search(pos):
    total = 2**len(pos)
    high = total -1
    low = 0
    for letter in pos:
        # print('letter: ' + letter)
        # print('high: ' + str(high))
        # print('low: ' + str(low))
        midpoint = (low + high) // 2
        # print('midpoint: ' + str(midpoint))
        # print('\n')
        # Lower half
        if letter == "F" or letter == "L":
            if midpoint == low:
                return low
            high = midpoint
        
        # Higher half
        if letter == "B" or letter == "R":
            if midpoint == low:
                return high
            low = midpoint + 1

def calc_seat_number(row, col):
    return row * 8 + col


if __name__ == "__main__":
    input = read_file()
    for seat in input:
        # print("--------")
        (binary_row, binary_col) = parse_input(seat)
        row = binary_search(binary_row)
        col = binary_search(binary_col)
        # print("--------\n")
        seat_number = calc_seat_number(row, col)
        taken_seats.add(seat_number)
    for x in range(801):
        if x not in taken_seats:
            print(x)


