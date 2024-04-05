def get_priority(item_type):
    return ord(item_type) - (96 if item_type >= "a" else 38)


with open("input.txt") as f:
    rucksacks = f.read().split("\n")

    sum = 0
    for item in rucksacks:
        split_index = len(item) // 2
        first_set, second_set = (set(item[:split_index]), set(item[split_index:]))
        duplicate = first_set.intersection(second_set).pop()
        priority = get_priority(duplicate)
        sum += priority

    print(sum)
