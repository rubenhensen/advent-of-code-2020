from itertools import combinations
from collections import deque
# print(list(combinations(range(5),2)))

filename = '9/input.txt'
preamble_size = 25

def read_file():
    with open(filename) as file:
        input =  file.readlines()
        stripped = deque()
        for line in input:
            stripped.append(int(line.strip('\n')))
        return stripped
            

if __name__ == "__main__":
    input = read_file()

    active = deque()
    for idx in range(preamble_size):
        active.append(input.popleft())

    while True:
        if not input:
            break
        sum_set = set()
        for i in combinations(active,2):
            sum_set.add(i[0] + i[1])


        check = input.popleft()
        if check not in sum_set:
            print(check)

        active.popleft()
        active.append(check)



    
    
