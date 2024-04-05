def get_priority(item):
    code_point = ord(item)
    if code_point >= ord("a") and code_point <= ord("z"):
        return code_point - 96

    return code_point - 64 + 26


with open("input.txt") as f:
    rucksacks = f.read().split("\n")

    sum = 0
    for item in rucksacks:
        split_index = int(len(item) / 2)
        first_set, second_set = (set(item[:split_index]), set(item[split_index:]))
        duplicate = first_set.intersection(second_set).pop()
        priority = get_priority(duplicate)
        sum += priority

    print(sum)
