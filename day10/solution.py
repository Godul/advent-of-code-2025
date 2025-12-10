from ortools.sat.python import cp_model

from collections import deque


def move(from_t: tuple, by_t: tuple):
    return tuple((x + y) % 2 for x, y in zip(from_t, by_t))


def find_shortest_path(transitions, target) -> int:
    q = deque()
    vis = set()
    start = (0,) * len(target)
    q.append((0, start))


    while len(q) > 0:
        dist, node = q.popleft()

        if node in vis:
            continue

        if node == target:
            return dist
    
        vis.add(node)
        
        for t in transitions:
            next_t = move(node, t)
            if next_t not in vis:
                q.append((dist + 1, next_t))
    return None    


def part_one():
    count = 0
    with open('input.txt') as file:
        for line in file:
            s = line.split()

            target = tuple(1 if ch == '#' else 0 for ch in s[0][1:-1])
            transitions = []
            for button in s[1:-1]:
                positions = set(map(int, button[1:-1].split(',')))
                trans = tuple(1 if idx in positions else 0 for idx in range(len(target)))
                transitions.append(trans)

            shortest_len = find_shortest_path(transitions, target)
            count += shortest_len
    print(count)


def solve_min_integer_combination(vectors, target):
    """
    Solve min sum(c_i) subject to sum_i c_i * vectors[i] == target
    vectors: list of lists or tuples of integers (0/1)
    target: list or tuple of integers
    Returns: list of coefficients c_i
    """
    m = len(target)       # length of each vector
    n = len(vectors)      # number of vectors

    model = cp_model.CpModel()

    # Decision variables: nonnegative integers
    x = [model.NewIntVar(0, sum(target), f"x_{i}") for i in range(n)]

    # Constraints: linear combination must match target
    for j in range(m):
        model.Add(sum(vectors[i][j] * x[i] for i in range(n)) == target[j])

    # Objective: minimize total sum of coefficients
    model.Minimize(sum(x))

    # Solve
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        solution = [solver.Value(var) for var in x]
        return sum(solution)
    else:
        return None


def part_two():
    count = 0
    with open('input.txt') as file:
        for line in file:
            s = line.split()

            target = tuple(map(int, s[-1][1:-1].split(',')))
    
            transitions = []
            for button in s[1:-1]:
                positions = set(map(int, button[1:-1].split(',')))
                trans = tuple(1 if idx in positions else 0 for idx in range(len(target)))
                transitions.append(trans)

            shortest_len = solve_min_integer_combination(transitions, target)
            count += shortest_len
    print(count)


if __name__ == '__main__':
    part_two()
