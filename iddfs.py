def depth_limited_search(graph, node, depth_limit, visited):
    if node not in visited:
        visited.append(node)

    if depth_limit == 0:
        return

    for neighbor in graph.get(node, []):
        depth_limited_search(graph, neighbor, depth_limit - 1, visited)


def iddfs(graph, start, max_depth):
    result = {}

    for depth in range(max_depth + 1):
        visited = []
        depth_limited_search(graph, start, depth, visited)
        result[depth] = visited

    return result
