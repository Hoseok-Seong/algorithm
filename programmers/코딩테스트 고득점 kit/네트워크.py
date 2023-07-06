def solution(n, computers):
    visited = [[0] * n for _ in range(n)]

    def dfs(node):
        visited[node][node] = 1
        for i in range(n):
            if computers[node][i] == 1 and visited[i][i] == 0:
                dfs(i)

    count = 0
    for i in range(n):
        if visited[i][i] == 0:
            dfs(i)
            count += 1

    return count