from collections import defaultdict


def dfs(node: int, graph: dict[id, list[id]], node_to_ways: dict[int, int], id_to_name: dict[int, str]) -> int:
    if id_to_name[node] == 'out':
        return 1

    if node in node_to_ways:
        return node_to_ways[node]
    
    result = 0
    for child in graph[node]:
        result += dfs(child, graph, node_to_ways, id_to_name)

    node_to_ways[node] = result
    return result


def part_one():
    name_to_id = {}
    id_to_name = {}
    graph = {}

    next_id = 0
    def register_node(name):
        nonlocal next_id
        if name not in name_to_id:
            name_to_id[name] = next_id
            id_to_name[next_id] = name
            next_id += 1
        return name_to_id[name]


    with open('input.txt', 'r') as file:
        for line in file:
            chunks = line.strip().split()
            source = chunks[0][:-1]
            targets = chunks[1:]

            source_id = register_node(source)
            target_ids = [register_node(t) for t in targets]

            graph[source_id] = target_ids
    
    node_to_ways = {}
    result = dfs(name_to_id['you'], graph, node_to_ways, id_to_name)
    print(result)


def dfs2(node: int, graph: dict[id, list[id]], node_to_ways: dict[int, dict[str, int]], id_to_name: dict[int, str]) -> dict[str, int]:
    name = id_to_name[node]
    if name == 'out':
        return {'none': 1}

    if node in node_to_ways:
        return node_to_ways[node]
    
    result = defaultdict(int)
    for child in graph[node]:
        child_results = dfs2(child, graph, node_to_ways, id_to_name)
        for k, v in child_results.items():
            result[k] += v

    if name == 'fft':
        result['fft'] = result['none']
        result['both'] = result['dac']
    elif name == 'dac':
        result['dac'] = result['none']
        result['both'] = result['fft']

    node_to_ways[node] = result
    return result


def part_two():
    name_to_id = {}
    id_to_name = {}
    graph = {}

    next_id = 0
    def register_node(name):
        nonlocal next_id
        if name not in name_to_id:
            name_to_id[name] = next_id
            id_to_name[next_id] = name
            next_id += 1
        return name_to_id[name]


    with open('input.txt', 'r') as file:
        for line in file:
            chunks = line.strip().split()
            source = chunks[0][:-1]
            targets = chunks[1:]

            source_id = register_node(source)
            target_ids = [register_node(t) for t in targets]

            graph[source_id] = target_ids
    
    node_to_ways = {}
    result = dfs2(name_to_id['svr'], graph, node_to_ways, id_to_name)
    print(result['both'])


if __name__ == '__main__':
    part_two()
