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
            
def find_small_big(dq):
    low = 9999999999999999
    high = 0
    for numb in dq:
        if numb > high:
            high = numb
        if numb < low:
            low = numb
    return (low, high)




if __name__ == "__main__":
    bad = 0
    input = read_file()
    copy = input.copy()

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
            bad = check
            # print(check)
            break

        active.popleft()
        active.append(check)

    dq = deque()
    while True:
        add = sum(dq)
        if add == bad:
            (small, big) = find_small_big(dq)
            print(dq)
            ans = str(small + big)
            print('bad: ' + ans)
            break
        if add > bad:
            dq.popleft()
        if add < bad:
            dq.append(copy.popleft())
        



    
    
