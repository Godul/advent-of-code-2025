import bisect


def merge_intervals(intervals: list[tuple[int, int]]):
    """Merge overlapping intervals. Assumes intervals are sorted."""
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            # No overlap, add as new interval
            merged.append((start, end))
        else:
            # Overlap, merge with the last interval
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    return merged


def is_in_interval(intervals: list[tuple[int, int]], id: list[int]) -> bool:
    ip = bisect.bisect(intervals, (id, id))
    if ip == 0:
        return None

    _, right = intervals[ip - 1]
    return right > id    


def part_one_and_two():
    intervals = []
    ids = []

    with open('input.txt', 'r') as file:
        while '-' in (line := file.readline()):
            b ,e = line.strip().split('-')
            intervals.append((int(b), int(e) + 1))
        
        for line in file.readlines():
            ids.append(int(line))
    
    
    intervals.sort()
    intervals = merge_intervals(intervals)

    count = 0
    for id in ids:
        if is_in_interval(intervals, id):
            count += 1
    print(f'part_one: {count}')

    count = 0
    for begin, end in intervals:
        count += end - begin
    print(f'part_two: {count}')


if __name__ == '__main__':
    part_one_and_two()
