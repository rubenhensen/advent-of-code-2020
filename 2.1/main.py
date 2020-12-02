# Using readlines() 
file1 = open('2.1/input.txt', 'r') 
lines = file1.readlines() 

valid_pass = 0

# Strips the newline character 
for line in lines: 
    x = line.split(" ")
    y = x[0].split("-")
    first_index = int(y[0]) - 1
    second_index = int(y[1]) - 1
    letter = x[1][0:1]
    passw = x[2]

    if (passw[first_index] == letter) != (passw[second_index] == letter):
        valid_pass += 1
    # print("count: " + str(count))

print("valid_pass: " + str(valid_pass))

    

