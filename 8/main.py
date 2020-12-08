import re

# parse_regex = re.compile("^(?P<color>\w* \w*) bags contain ((\d \w* \w*) bag.?[,\.].?)*|(no other bags.)$")
onebag_re = re.compile("(?P<instruction>\w*) (?P<sign>.)(?P<number>\d*)")

filename = '8/input.txt'
bag_dict = dict()



def read_file():
    with open(filename) as file:
        return file.readlines()

def follow_instruction(instruction_list, index):
    (instruction, sign, number) = instruction_list[index]
    number = int(number)
    
    if instruction == 'nop':
        return (0, index + 1)
    if instruction == 'acc' and sign == '+':
        return (number, index + 1)
    if instruction == 'acc' and sign == '-':
        return (-number, index + 1)
    if instruction == 'jmp' and sign == '+':
        return (0, index + number)
    if instruction == 'jmp' and sign == '-':
        return (0, index - number)
    print("did nothing")
    return (0,0)


if __name__ == "__main__":
    input = read_file()
    
    stripped_input = []
    for line in input:
        groups = onebag_re.search(line).groups()
        stripped_input.append(groups)
    # print(stripped_input)

    loop_set = set()
    accumelator = 0
    idx = 0
    while True:
        if idx in loop_set:
            break
        
        loop_set.add(idx)
        (acc, idx) = follow_instruction(stripped_input, idx)
        accumelator += int(acc)

    print(accumelator)
