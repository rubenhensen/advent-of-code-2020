import math
filename = '10/input.txt'

def read_file():
    with open(filename) as file:
        input =  file.readlines()
        stripped = [0]
        for line in input:
            stripped.append(int(line.strip('\n')))
        stripped.sort()
        highest = stripped[-1]
        stripped.append(highest + 3)
        return stripped

def tribonnaci(known, nr):
    # print('in tribonnaci')
    # print(nr)
    for x in range(nr):
        print(x)
        if x+1 > len(known):
            known.append(known[x-1] + known[x-2] + known[x-3])
    
    return (known, known[nr-1])

            

if __name__ == "__main__":
    input = read_file()
    nr_one_jolts = [] 
    known = [2,4,7,13]
    one_jolt = 0
    for x in range(len(input)-1):
        if x == 0:
            print('skip')
        elif input[x + 1] - input[x] == 1 and input[x] - input[x - 1] == 1:
            one_jolt += 1
        elif input[x + 1] - input[x] == 3 or input[x] - input[x - 1] == 3:
            if one_jolt != 0:
                nr_one_jolts.append(one_jolt)
                one_jolt = 0

    nr_one_jolts_comb = []
    for nr in nr_one_jolts:
        (arr, ans) = tribonnaci(known, nr)
        known = arr
        nr_one_jolts_comb.append(ans)
    
    
    
    result = math.prod(nr_one_jolts_comb)
    print(result)
                
    # print(one_jolt)
    # print(three_jolt)
    # print(one_jolt*three_jolt)





    
    
