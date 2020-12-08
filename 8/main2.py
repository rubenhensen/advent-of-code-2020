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

def follow_instruction_switched(instruction_list, index):
    (instruction, sign, number) = instruction_list[index]
    number = int(number)

    if instruction == 'nop' and sign == '+':
        return (0, index + number)
    if instruction == 'nop' and sign == '-':
        return (0, index - number)
    if instruction == 'acc' and sign == '+':
        return (number, index + 1)
    if instruction == 'acc' and sign == '-':
        return (-number, index + 1)
    if instruction == 'jmp':
        return (0, index + 1)
    print("did nothing")
    return (0,0)
    
def loop(switch):
    loop_set = set()
    accumelator = 0
    idx = 0
    while True:
        if idx in loop_set:
            # print("Loop")
            return 0
        if idx >= len(stripped_input):
            print("End")
            return accumelator
        
        loop_set.add(idx)
        if idx == switch:
            (acc, idx) = follow_instruction_switched(stripped_input, idx)
        else:
            (acc, idx) = follow_instruction(stripped_input, idx)

        accumelator += int(acc)


if __name__ == "__main__":
    input = read_file()
    
    stripped_input = []
    for line in input:
        groups = onebag_re.search(line).groups()
        stripped_input.append(groups)

    for i in range(len(stripped_input)):
        acc = loop(i)
        if acc != 0:
            print(acc)
    
    
    
