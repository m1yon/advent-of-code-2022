with open("input.txt") as f:
    lines = f.read().split("\n")

    parsed_lines = [
        [
            tuple(map(int, section_range.split("-")))
            for section_range in tuple(line.split(","))
        ]
        for line in lines
        if len(line) > 0
    ]

    count = 0

    for elf_1, elf_2 in parsed_lines:
        start_section_1, end_section_1 = elf_1
        start_section_2, end_section_2 = elf_2

        if max(start_section_1, start_section_2) <= min(end_section_1, end_section_2):
            count += 1

    print(count)
