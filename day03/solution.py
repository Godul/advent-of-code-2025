def max_bank_value_1(bank: str):
    length = len(bank)
    max_digit = ['1'] * length
    max_digit[-1] = bank[-1]

    max_value = 0
    for i in reversed(range(length - 1)):
        value = int(bank[i]) * 10 + int(max_digit[i + 1])
        max_value = max(max_value, value)
        max_digit[i] = max(bank[i], max_digit[i + 1])
    return max_value


def max_bank_value_2(bank: str):
    L = len(bank)
    N = 12

    t = [[0] * L for _ in range(N + 1)]
    
    t[1][-1] = int(bank[-1])

    for n in range(1, N + 1):
        for i in range(L - max(2, n), -1, -1):
            t[n][i] = max(10**(n - 1) * int(bank[i]) + t[n - 1][i + 1], t[n][i + 1])
    return t[12][0]


def find_max_value(eval_func):
    with open('input.txt', 'r') as file:
        data = file.readlines()
    
    result = 0
    for line in data:
        digits = line.strip()
        bank_val = eval_func(digits)
        result += bank_val
    print(result)


def part_one():
    find_max_value(max_bank_value_1)


def part_two():
    find_max_value(max_bank_value_2)


if __name__ == '__main__':
    part_two()
