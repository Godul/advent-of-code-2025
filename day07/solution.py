def part_one_and_two():
    with open('input.txt', 'r') as file:
        line = file.readline()
        idx = line.find('S')
        
        beams = set([idx])
        next_beams = set()

        sources_arr = [0] * (len(line) - 1)
        sources_arr[idx] = 1
        next_sources_arr = [0] * len(sources_arr)

        split_count = 0

        for line in file:
            split_pos = [idx for idx in range(len(line) - 1) if line[idx] == '^']

            for pos in split_pos:
                if pos in beams:
                    split_count += 1
                    beams.remove(pos)

                    if pos - 1 >= 0:
                        next_beams.add(pos - 1)
                        next_sources_arr[pos - 1] += sources_arr[pos]
                    if pos + 1 < len(line) - 1:
                        next_beams.add(pos + 1)
                        next_sources_arr[pos + 1] += sources_arr[pos]

            for idx in beams:
                next_beams.add(idx)
                next_sources_arr[idx] += sources_arr[idx]

            beams = next_beams
            next_beams = set()

            sources_arr, next_sources_arr = next_sources_arr, sources_arr
            for i in range(len(next_sources_arr)):
                next_sources_arr[i] = 0

    print(f'part_one={split_count}')
    print(f'part_two={sum(sources_arr)}')


if __name__ == '__main__':
    part_one_and_two()
