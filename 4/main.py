import re
length_regex = re.compile("^(?P<numbers>\d*)(?P<letters>\w*)$")
# hcl_regex = re.compile("^(?P<hex>#\n*)$")
hcl_regex = re.compile("^(?P<hex>#\w*)")
pid_regex = re.compile("^(?P<number>\d*)")
ecl = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
filepath = '4/input.txt'
valid_passport = 0

def reset_passport(passp):
    for key in passp:
        passp[key] = ''

def check_passport(passp):
    for key in passp:

        if passp[key] == '' and key != "cid":
            return False

        if key == "byr":
            
            if int(passp[key]) < 1920 or int(passp[key]) > 2002:
                # print("byr false")
                return False

        if key == "iyr":
            
            if int(passp[key]) < 2010 or int(passp[key]) > 2020:
                # print("iyr false")
                return False

        if key == "eyr":
            
            if int(passp[key]) < 2020 or int(passp[key]) > 2030:
                # print("eyr false")
                return False
        
        if key == "hgt":
            # print(passp[key])
            (numbers, letters) = length_regex.search(passp[key]).groups()
            numbers = int(numbers)
            print(numbers)
            print(letters)
            if letters == "cm":
                if numbers < 150 or numbers > 193:
                    print("hgt cm false")
                    return False
            elif letters == "in":
                if numbers < 59 or numbers > 76:
                    print("hgt in false")
                    return False
            else:
                return False
        
        if key == "hcl":
            # print(passp[key])
            match = hcl_regex.search(passp[key])
            if not match or len(passp[key]) != 7:
                # print("hcl false")
                return False
        
        if key == "ecl":
            # print(passp[key])
            if passp[key] not in ecl:
                # print("ecl false")
                return False

        if key == "pid":
            # print(passp[key])
            match = pid_regex.search(passp[key])
            if not match or len(passp[key]) != 9:
                # print("pid false")
                return False
            
    return True


passport = {
    "byr" : '',
    "iyr" : '',
    "eyr" : '',
    "hgt" : '',
    "hcl" : '',
    "ecl" : '',
    "pid" : '',
    "cid" : ''
}

# readlines stopped one line early?
with open(filepath) as file:
    lines = file.readlines()
    for line in lines:
        # print(repr(line))
        if line == "\n":
            if check_passport(passport):
                valid_passport += 1
                # print(True)
            reset_passport(passport) 
        else: 
            words = line.split(" ")
            for word in words:
                split = word.split(":")
                id = split[0]
                value = split[1]
                passport[id] = value.strip('\n')
                # print(passport) 

print("Valid passports: " + str(valid_passport))
        



