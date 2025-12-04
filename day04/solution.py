def load_matrix() -> list[list[str]]:
    matrix = []
    with open('input.txt', 'r') as file:
        for line in  file.readlines():
            matrix.append([x for x in line.strip()])
    return matrix


def count_adjacent_rolls(matrix: list[str] | list[list[str]], i: int, j: int):
    rolls_n = 0
    for i_d, j_d in (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1)
    ):
        if 0 <= i + i_d < len(matrix) and 0 <= j + j_d < len(matrix[0]):
            if matrix[i + i_d][j + j_d] == '@':
                rolls_n += 1
    return rolls_n


def part_one():
    matrix = load_matrix()
    
    accessible_rolls = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != '@':
                continue
            rolls_n = count_adjacent_rolls(matrix, i, j)
            if rolls_n < 4:
                accessible_rolls += 1
    print(accessible_rolls)
            

def part_two():
    matrix = load_matrix()
    
    result = 0
    keep_going = True

    while keep_going:
        acc_rolls = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != '@':
                    continue
                rolls_n = count_adjacent_rolls(matrix, i, j)
                if rolls_n < 4:
                    matrix[i][j] = '.'
                    acc_rolls += 1
        
        result += acc_rolls
        if acc_rolls == 0:
            keep_going = False
    
    print(result)


if __name__ == '__main__':
    part_two()
