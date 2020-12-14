filename = '12/input.txt'
boat_direction = 'E'
x = 0
y = 0

def read_file():
    with open(filename) as file:
        input =  file.readlines()
        parsed = []
        for line in input:
            line = line.strip('\n')
            dir = line[0]
            unit = line[1:]
            parsed.append((dir,unit))
            
        return parsed

def go_cardinal(dir, unit):
    global x, y
    if dir == 'N':
        y += int(unit)

    if dir == 'E':
        x += int(unit)
    
    if dir == 'S':
        y -= int(unit)
    
    if dir == 'W':
        x -= int(unit)
            

def find_cardinal(dir, unit):
    global boat_direction
    if dir == 'L' and boat_direction == 'N':
        if unit == '90':
            boat_direction = 'W'
        if unit == '180':
            boat_direction = 'S'
        if unit == '270':
            boat_direction = 'E'
    elif dir == 'R' and boat_direction == 'N':
        if unit == '90':
            boat_direction = 'E'
        if unit == '180':
            boat_direction = 'S'
        if unit == '270':
            boat_direction = 'W'

    elif dir == 'L' and boat_direction == 'E':
        if unit == '90':
            boat_direction = 'N'
        if unit == '180':
            boat_direction = 'W'
        if unit == '270':
            boat_direction = 'S'
    elif dir == 'R' and boat_direction == 'E':
        if unit == '90':
            boat_direction = 'S'
        if unit == '180':
            boat_direction = 'W'
        if unit == '270':
            boat_direction = 'N'

    elif dir == 'L' and boat_direction == 'S':
        if unit == '90':
            boat_direction = 'E'
        if unit == '180':
            boat_direction = 'N'
        if unit == '270':
            boat_direction = 'W'
    elif dir == 'R' and boat_direction == 'S':
        if unit == '90':
            boat_direction = 'W'
        if unit == '180':
            boat_direction = 'N'
        if unit == '270':
            boat_direction = 'E'

    elif dir == 'L' and boat_direction == 'W':
        if unit == '90':
            boat_direction = 'S'
        if unit == '180':
            boat_direction = 'E'
        if unit == '270':
            boat_direction = 'N'
    elif dir == 'R' and boat_direction == 'W':
        if unit == '90':
            boat_direction = 'N'
        if unit == '180':
            boat_direction = 'E'
        if unit == '270':
            boat_direction = 'S'




        
# seats[row][col]
if __name__ == "__main__":
    parsed = read_file()
    print(parsed)

    for instruction in parsed:
        dir = instruction[0]
        unit = instruction[1]

        if dir == 'L' or dir == 'R':
            find_cardinal(dir, unit)
        elif dir == 'F':
            go_cardinal(boat_direction,unit)
        else:
            go_cardinal(dir, unit)
    
    manhatten = abs(x) + abs(y)
    print(manhatten)

    
    
