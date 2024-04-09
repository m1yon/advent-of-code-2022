with open("input.txt") as f:
    lines = f.read().rstrip().split("\n")

    stack_label_line_index = next(
        (
            index
            for index in range(len(lines))
            if not lines[index].strip().startswith("[")
        ),
        0,
    )

    number_of_stacks = int(lines[stack_label_line_index].rstrip()[-1])

    stacks = [[] for _ in range(number_of_stacks)]

    for line in lines[:stack_label_line_index]:
        for current_stack in range(number_of_stacks):
            index = current_stack * 4 + 1

            if index >= len(line):
                continue

            value = line[current_stack * 4 + 1]

            if value != " ":
                stacks[current_stack].insert(0, value)

    commands_start_line_index = stack_label_line_index + 2
    commands = lines[commands_start_line_index:]

    for command in commands:
        _, move_amount_str, _, from_stack_str, _, to_stack_str = command.split(" ")
        move_amount = int(move_amount_str)
        from_stack = stacks[int(from_stack_str) - 1]
        to_stack = stacks[int(to_stack_str) - 1]

        move_index = move_amount * -1

        to_stack.extend(from_stack[move_index:])
        stacks[int(from_stack_str) - 1] = from_stack[:move_index]

    result = "".join(stack[-1] for stack in stacks)

    print(result)
