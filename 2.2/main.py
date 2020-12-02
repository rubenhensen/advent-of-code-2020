# Using readlines() 
file1 = open('2.1/input.txt', 'r') 
lines = file1.readlines() 

valid_pass = 0

# Strips the newline character 
for line in lines: 
    x = line.split(" ")
    y = x[0].split("-")
    min_number = int(y[0])
    max_number = int(y[1])
    letter = x[1][0:1]
    passw = x[2]
    # print("min_number: " + str(min_number))
    # print("max_number: " + str(max_number))
    # print("letter: " + letter)
    # print("passw: " + passw)
    count = 0
    for char in passw:
        if char == letter:
            count += 1
    if count >= min_number and count <= max_number:
        valid_pass += 1
    # print("count: " + str(count))

print("valid_pass: " + str(valid_pass))

    

