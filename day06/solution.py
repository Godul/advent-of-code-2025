import math


def day_one():
    with open('input.txt', 'r') as file:
        line = file.readline()
        arr = [[int(x)] for x in line.strip().split()]

        while (line := file.readline())[0].isdigit():
            for i, x in enumerate(line.strip().split()):
                arr[i].append(int(x))
    
    operations = line.strip().split()
    
    result = 0
    for i, op in enumerate(operations):
        if op == '+':
            result += sum(arr[i])
        elif op == '*':
            result += math.prod(arr[i])
        else:
            assert False

    print(result)


def find_if(s, predicate, start: int):
    for i, c in enumerate(s[start:], start):
        if predicate(c):
            return i
    return None


def has_digit(s: str) -> bool:
    return any(ch.isdigit() for ch in s)


def day_two():
    with open('input.txt', 'r') as file:
        line = file.readline()
        arr = [ch for ch in line[:-1]]
        for line in file:
            if not has_digit(line):
                break

            for i, ch in enumerate(line[:-1]):
                arr[i] = arr[i] + ch

    count = 0
    i = 0
    keep_going = True
    while keep_going:
        j = find_if(line, lambda x: x == '+' or x == '*', i + 1)
        if j is None:
            j = len(line)
            keep_going = False

        numbers = [int(s) for s in arr[i:j-1]]

        if line[i] == '*':
            count += math.prod(numbers)
        elif line[i] == '+':
            count += sum(numbers)
        else:
            assert False
        i = j
            
    print(count)     


if __name__ == '__main__':
    day_two()
