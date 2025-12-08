import math


def dist(p1: tuple[int, int, int], p2: tuple[int, int, int]):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2


def part_one():
    coords = []
    with open('input.txt', 'r') as file:
        for line in file:
            x, y, z = line.strip().split(',')
            coords.append((int(x), int(y), int(z)))
    
    arr = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            p1 = coords[i]
            p2 = coords[j]
            d = dist(p1, p2)
            arr.append((d, i, j))
    arr.sort()

    point_to_group = {p: (p, set([p])) for p in range(len(coords))}

    for (d, p1, p2) in arr[:1000]:
        id1, g1 = point_to_group[p1]
        id2, g2 = point_to_group[p2]

        if id1 == id2:
            continue

        new_g = g1.union(g2)
        for p in new_g:
            point_to_group[p] = (id1, new_g)

    id_to_group = {}
    for id, group in point_to_group.values():
        id_to_group[id] = group

    sorted_sizes = sorted(map(len, id_to_group.values()), reverse=True)
    print(math.prod(sorted_sizes[:3]))


def part_two():
    coords = []
    with open('input.txt', 'r') as file:
        for line in file:
            x, y, z = line.strip().split(',')
            coords.append((int(x), int(y), int(z)))
    
    arr = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            p1 = coords[i]
            p2 = coords[j]
            d = dist(p1, p2)
            arr.append((d, i, j))
    arr.sort()

    point_to_group = {p: (p, set([p])) for p in range(len(coords))}

    connected = 0
    for (d, p1, p2) in arr:
        id1, g1 = point_to_group[p1]
        id2, g2 = point_to_group[p2]

        if id1 == id2:
            continue

        new_g = g1.union(g2)
        for p in new_g:
            point_to_group[p] = (id1, new_g)
        
        connected += 1
        if connected == 999:
            print(coords[p1][0] * coords[p2][0])
            break


if __name__ == '__main__':
    part_two()
