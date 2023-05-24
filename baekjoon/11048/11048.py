n, m = map(int, input().split())

candies = [list(map(int, input().split())) for i in range(n)]

# 1, 1부터 시작이므로 1 더 큰 2차원 배열 생성
result = [[0] * (m+1) for i in range(n+1)]

for x in range(1, n+1):
    for y in range(1, m+1):
        result[x][y] = max(result[x-1][y], result[x][y-1], result[x-1][y-1]) + candies[x-1][y-1]

print(result[n][m])