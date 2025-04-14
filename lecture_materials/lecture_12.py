



def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')  # travers from the vertex

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        if (
            r < 0 or r >= rows or
            c < 0 or c >= cols or
            grid[r][c] == '0' or
            visited[r][c]
        ):
            return
        visited[r][c] = True
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and not visited[r][c]:
                dfs(r, c)
                count += 1

    return count



from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print("Visit:", vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)





from collections import deque

def fill_grid(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    empty = 0
    # Fill the queue with bacteria starting points
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'B':
                queue.append((r, c, 0))  # coordinates + time
            elif grid[r][c] == '.':
                empty += 1

    return rows, cols, queue, empty


def min_hours_to_infect(grid):
    rows, cols, queue, empty = fill_grid(grid)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_time = 0

    while queue:
        r, c, time = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '.':
                grid[nr][nc] = 'B'
                empty -= 1
                queue.append((nr, nc, time + 1))
                max_time = max(max_time, time + 1)

    return max_time if empty == 0 else -1
