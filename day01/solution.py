def part_one():
    with open('input.txt', 'r') as file:
        data = file.readlines()

    pos = 50
    zeros_count = 0

    for line in data:
        direction = line[0]
        steps = int(line[1:])
    
        if direction == 'R':
            pos = (pos + steps) % 100
        elif direction == 'L':
            pos = (pos - steps) % 100

        if pos == 0:
            zeros_count += 1

    print(zeros_count)


def part_two():
    with open('input.txt', 'r') as file:
        data = file.readlines()
    
    pos = 50
    zeros_count = 0
    
    for line in data:
        direction = line[0]
        steps = int(line[1:])

        if direction == 'R':
            new_pos = pos + steps
            zeros_count += new_pos // 100 - pos // 100
            pos = new_pos % 100
        elif direction == 'L':
            new_pos = pos - steps
            if new_pos <= 0 and pos > 0:
                zeros_count += 1
            zeros_count += abs(new_pos) // 100
            pos = new_pos % 100

    print(zeros_count)


if __name__ == '__main__':
    part_two()
