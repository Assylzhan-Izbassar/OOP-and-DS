def dfs(graph, start, num=1, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(str(num) + ' ' + start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, num + 1, visited)

graph = {
    'v1': ['v2', 'v3'],
    'v2': ['v1', 'v3'],
    'v3': ['v1', 'v4'],
    'v4': ['v3']
}

dfs(graph, 'v1')
