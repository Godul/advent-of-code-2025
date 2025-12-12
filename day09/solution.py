import sys


def calc_area(p1: tuple[int, int], p2: tuple[int, int]):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def part_one():
    coords = []
    with open('input.txt', 'r') as file:
        for line in file:
            x, y = line.split(',')
            coords.append((int(x), int(y)))
    
    max_area = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            area = calc_area(coords[i], coords[j])
            max_area = max(area, max_area)

    print(max_area)


def compress_coords(coords: list[tuple[int, int]]):
    x_orig = []
    y_orig = []
    x_comp = {}
    y_comp = {}

    xs = sorted(x for x, _ in coords)
    ys = sorted(y for _, y in coords)
    
    for x in xs:
        if x not in x_comp:
            x_comp[x] = len(x_orig)
            x_orig.append(x)

    for y in ys:
        if y not in y_comp:
            y_comp[y] = len(y_orig)
            y_orig.append(y)
    
    coords_c = [(x_comp[x], y_comp[y]) for x, y in coords]
    return coords_c, x_orig, y_orig


def find_point_inside(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[0]) - 1):
            if matrix[x][y] == 'X':
                break
            if matrix[x][y] == '#':
                assert matrix[x][y + 1] != '.'
                if x - 1 >= 0 and matrix[x - 1][y] != '.' and matrix[x - 1][y + 1] == '.':
                    return x - 1, y + 1
                if x + 1 < len(matrix) and matrix[x + 1][y] != '.' and matrix[x + 1][y + 1] == '.':
                    return x + 1, y + 1
                break
    return None, None


def dfs(x, y, matrix):
    if matrix[x][y] != '.':
        return

    matrix[x][y] = '&'

    if x - 1 >= 0:
        dfs(x - 1, y, matrix)
    if x + 1 < len(matrix):
        dfs(x + 1, y, matrix)
    if y - 1 >= 0:
        dfs(x, y - 1, matrix)    
    if y + 1 < len(matrix[0]):
        dfs(x, y + 1, matrix)


def check_if_inside(p1: tuple[int, int], p2: tuple[int, int], matrix: list[list[str]]) -> bool:
    x1, y1 = p1
    x2, y2 = p2
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if matrix[x][y] == '.':
                return False
    return True


def calc_area_2(p1: tuple[int, int], p2: tuple[int, int], x_orig: list[int], y_orig: list[int]):
    x1 = x_orig[p1[0]]
    x2 = x_orig[p2[0]]
    y1 = y_orig[p1[1]]
    y2 = y_orig[p2[1]]
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def part_two():
    coords = []
    with open('input.txt', 'r') as file:
        for line in file:
            x, y = line.split(',')
            coords.append((int(x), int(y)))

    coords, x_orig, y_orig = compress_coords(coords)
    matrix = [['.'] * len(y_orig) for _ in range(len(x_orig))]

    for x, y in coords:
        matrix[x][y] = '#'

    for p1, p2 in zip(coords, coords[1:] + [coords[0]]):
        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(y1 + 1, y2):
                matrix[x1][y] = 'X'
        if y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1 + 1, x2):
                matrix[x][y1] = 'X'


    x_start, y_start = find_point_inside(matrix)

    sys.setrecursionlimit(100000)  # Increase recursion limit for deep DFS
    dfs(x_start, y_start, matrix)

    max_area = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            p1, p2 = coords[i], coords[j]
            if not check_if_inside(p1, p2, matrix):
                continue

            area = calc_area_2(p1, p2, x_orig, y_orig)
            max_area = max(area, max_area)

    print(max_area)


if __name__ == '__main__':
    part_two()
