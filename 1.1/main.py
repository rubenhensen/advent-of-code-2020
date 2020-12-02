
# Using readlines() 
file1 = open('1.1/input.txt', 'r') 
lines = file1.readlines() 
  
# Strips the newline character 
for line in lines: 
    for line2 in lines: 
        x = int(line)
        y = int(line2)
        z = x + y
        # print(z)
        if z == 2020:
            print(x)
            print(y)
            print(x*y)
    


