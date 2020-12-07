import re

# parse_regex = re.compile("^(?P<color>\w* \w*) bags contain ((\d \w* \w*) bag.?[,\.].?)*|(no other bags.)$")
onebag_re = re.compile("(?P<number>\d)? ?(?P<color>\w* \w*) bags?")

filename = '7/input.txt'
bag_dict = dict()



def read_file():
    with open(filename) as file:
        return file.readlines()

def check_bag_recursively(inner_bags, count):
    if not inner_bags:
        return 0

    arr = []
    for bag in inner_bags:
        inner = check_bag_recursively(bag_dict[bag[1]], count)
        count = int(bag[0]) * inner + int(bag[0])
        arr.append(count)

    return sum(arr) 



if __name__ == "__main__":
    input = read_file()

    for line in input:
        # Parse line into groups
        groups = onebag_re.findall(line)

        # Get main bag color
        main_bag_color = groups.pop(0)[1]

        # Add bag to dictionary
        bag_dict[main_bag_color] = []

        for inner_bag in groups:
            if inner_bag[1] != 'no other':
                bag_dict[main_bag_color].append(inner_bag)

    # Check all bags except shiny gold recursively
    
    final_count = check_bag_recursively(bag_dict['shiny gold'], 0)

    print(final_count)


