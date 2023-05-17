def dfs(x, y):
    global count
    if x < 0 or x >= N or y < 0 or y >= N or grid[x][y] == 0:
        return
    grid[x][y] = 0  # 방문한 집은 0으로 표시
    count += 1
    dfs(x-1, y)  # 상
    dfs(x+1, y)  # 하
    dfs(x, y-1)  # 좌
    dfs(x, y+1)  # 우

N = int(input())
grid = [list(map(int, input().strip())) for _ in range(N)]
counts = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            count = 0
            dfs(i, j)
            counts.append(count)

counts.sort()
print(len(counts))
for count in counts:
    print(count)
