import re

# parse_regex = re.compile("^(?P<color>\w* \w*) bags contain ((\d \w* \w*) bag.?[,\.].?)*|(no other bags.)$")
onebag_re = re.compile("(?P<number>\d)? ?(?P<color>\w* \w*) bags?")

filename = '7/input.txt'
bag_dict = dict()



def read_file():
    with open(filename) as file:
        return file.readlines()

def check_bag_recursively(inner_bags):
    if not inner_bags:
        return False

    for bag in inner_bags:
        if bag == 'shiny gold':
            return True
        if check_bag_recursively(bag_dict[bag]):
            return True
    return False



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
            inner_bag_color = inner_bag[1]
            if inner_bag_color != 'no other':
                bag_dict[main_bag_color].append(inner_bag_color)

    # Check all bags except shiny gold recursively
    gold_bag_count = 0
    for i in bag_dict:
        if i != 'shiny gold':
            contains_gold = check_bag_recursively(bag_dict[i])
            if contains_gold:
                gold_bag_count += 1

    print(gold_bag_count)


