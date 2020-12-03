def check_slope(right, down):
    with open('3.1/input.txt') as file:
        lines = file.readlines()
        line_length = len(lines[0]) - 1
        total_index = 0
        trees_hit = 0
        slope = right
        lines = lines[::down]
        for line in lines:
            rel_index = total_index % line_length
            if line[rel_index] == '#':
                trees_hit += 1
            total_index += slope
        return trees_hit

with open('3.1/input.txt') as file:
    a = check_slope(1, 1)
    b = check_slope(3, 1)
    c = check_slope(5, 1)
    d = check_slope(7, 1)
    e = check_slope(1, 2)
    print(a)
    ans = a*b*c*d*e
    print(ans)

