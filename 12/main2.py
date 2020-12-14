filename = '12/input.txt'
boat_direction = 'E'
boat_x = 0
boat_y = 0
waypoint_x = 10
waypoint_y = 1

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

def move_waypoint(dir, unit):
    global waypoint_x, waypoint_y
    if dir == 'N':
        waypoint_y += int(unit)

    if dir == 'E':
        waypoint_x += int(unit)
    
    if dir == 'S':
        waypoint_y -= int(unit)
    
    if dir == 'W':
        waypoint_x -= int(unit)
            
def move_boat():
    global waypoint_x, waypoint_y, boat_x, boat_y
    boat_x += waypoint_x
    boat_y += waypoint_y

def rotate_waypoint(dir, unit):
    if dir == "R" and unit == "90":
        rotate_right()
    elif dir == "R" and unit == "180":
        rotate_right()
        rotate_right()
    elif dir == "R" and unit == "270":
        rotate_right()
        rotate_right()
        rotate_right()

    elif dir == "L" and unit == "90":
        rotate_right()
        rotate_right()
        rotate_right()
    elif dir == "L" and unit == "180":
        rotate_right()
        rotate_right()
    elif dir == "L" and unit == "270":
        rotate_right()



def rotate_right():
    global waypoint_x, waypoint_y
    new_x = waypoint_y
    new_y = waypoint_x * -1

    waypoint_x = new_x
    waypoint_y = new_y




if __name__ == "__main__":
    parsed = read_file()
    # print(parsed)

    for instruction in parsed:
        dir = instruction[0]
        unit = instruction[1]

        if dir == 'L' or dir == 'R':
            rotate_waypoint(dir, unit)
        elif dir == 'F':
            for i in range(int(unit)):
                move_boat()
        else:
            move_waypoint(dir, unit)
    
    manhatten = abs(boat_x) + abs(boat_y)
    print(manhatten)

    
    
