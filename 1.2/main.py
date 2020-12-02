
# Using readlines() 
file1 = open('1.2/input.txt', 'r') 
lines = file1.readlines() 
  
# Strips the newline character 
for line in lines: 
    for line2 in lines: 
        for line3 in lines: 
            x = int(line)
            y = int(line2)
            p = int(line3)
            z = x + y + p 
            if z == 2020:
                print(x*y*p)
    


