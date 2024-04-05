def get_priority(item_type):
    return ord(item_type) - (96 if item_type >= "a" else 38)


with open("input.txt") as f:
    rucksacks = f.read().split("\n")

    sum = 0
    for index in range(0, len(rucksacks) - 2, 3):
        closing_index = index + 3
        first_set, second_set, third_set = map(set, rucksacks[index:closing_index])
        duplicate = first_set.intersection(second_set, third_set).pop()

        priority = get_priority(duplicate)
        sum += priority

    print(sum)
