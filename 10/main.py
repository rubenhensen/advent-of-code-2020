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
            

if __name__ == "__main__":
    input = read_file()
    # print(input)
    one_jolt = 0
    three_jolt = 0
    for x in range(len(input)-1):
        if input[x + 1] - input[x] == 1:
            one_jolt += 1
        if input[x + 1] - input[x] == 3:
            three_jolt += 1
                
    print(one_jolt)
    print(three_jolt)
    print(one_jolt*three_jolt)





    
    
