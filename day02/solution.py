def sum_invalid_ids(begin_str: str, end_str: str) -> int:
    s = 0

    begin = int(begin_str)
    end = int(end_str)

    begin_half = int(begin_str[:len(begin_str) // 2]) if len(begin_str) > 1 else int(begin_str)
    end_half = int(end_str[:(len(end_str) + 1) // 2])

    for half in range(begin_half, end_half + 1):
        id = int(str(half) + str(half))
        if id >= begin and id <= end:
            s += id
    return s


def part_one():
    with open('input.txt', 'r') as file:
        data = file.read()
    
    s = 0
    for interval_str in data.strip().split(','):
        i_start, i_end = interval_str.split('-')
        s += sum_invalid_ids(i_start, i_end)
    print(s)


def sum_invalid_ids_2(begin_str: str, end_str: str):
    s = 0
    begin = int(begin_str)
    end = int(end_str)
    begin_len = len(begin_str)
    end_len = len(end_str)

    val_set = set()

    for word_len in range(begin_len, end_len + 1):
        for token_len in range(1, word_len // 2 + 1):
            if word_len % token_len == 0:
                token_n = word_len // token_len
                token_begin = 10**(token_len - 1)
                token_end = 10**token_len - 1
                for token in range(token_begin, token_end + 1):
                    word = str(token) * token_n
                    val = int(word)
                    if begin <= val <= end and val not in val_set:
                        s += val
                        val_set.add(val)
    return s


def part_two():
    with open('input.txt', 'r') as file:
        data = file.read()

    s = 0
    for interval_str in data.strip().split(','):
        i_start, i_end = interval_str.split('-')
        s += sum_invalid_ids_2(i_start, i_end)
    print(s)


if __name__ == '__main__':
    part_two()
