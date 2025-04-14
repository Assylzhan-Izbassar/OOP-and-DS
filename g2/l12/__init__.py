graph = {
    'A': ['B', 'D'],
    'B': ['A', 'D', 'E', 'C'],
    'C': ['B', 'E'],
    'D': ['A', 'B', 'E'],
    'E': ['D', 'B', 'C']
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start, end=' -> ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

dfs(graph, 'A')