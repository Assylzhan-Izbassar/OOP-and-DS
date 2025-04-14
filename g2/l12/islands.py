grid = [[1, 1, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 1, 1]]


def dfs(r, c):
    if r < 0 or r >= len(grid) \
            or c < 0 or c >= len(grid[r]) \
        or grid[r][c] == 0 or visited[r][c]:
        return
    visited[r][c] = True
    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)

row, col = len(grid), len(grid[0])
visited = [[False] * col for _ in range(row)]

print(visited)

component = 0
for i in range(row):
    for j in range(col):
        if grid[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            component += 1

for i in range(row):
    for j in range(col):
        print(visited[i][j], end=' ')
    print()
print(component)

