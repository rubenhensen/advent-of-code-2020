import re

filename = '6/input.txt'
answer_count = []

def read_file():
    with open(filename) as file:
        return file.readlines()


if __name__ == "__main__":
    input = read_file()
    ans_set = set()
    for line in input:
        line = line.strip('\n')

        if line == "":
            answer_count.append(len(ans_set))
            ans_set = set()

        for letter in line:
            ans_set.add(letter)

    answer_count.append(len(ans_set))

    print(sum(answer_count))
