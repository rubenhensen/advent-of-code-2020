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
            if "empty" not in ans_set:
                answer_count.append(len(ans_set))
            ans_set = set()

        if not ans_set:
            for letter in line:
                ans_set.add(letter) 
        else:
            ans_set_copy = ans_set
            ans_set = set()
            
            for letter in line:
                if letter in ans_set_copy:
                    ans_set.add(letter)
            
            if not ans_set:
                ans_set.add("empty")

    answer_count.append(len(ans_set))
    print(answer_count)
    print(sum(answer_count))
