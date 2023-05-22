import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

# 초기 배열
array = [list(map(int, input().split())) for _ in range(n)]

# 최대수
maxNumber = max(map(max, array))

# 임시 배열
temp_array = [[0] * n for _ in range(n)]

# 물에 잠기는 영역 구분
def area(number):
    for i in range(n):
        for j in range(n):
            if array[i][j] < number:
                temp_array[i][j] = 1  # 물 잠김
            if array[i][j] >= number:
                temp_array[i][j] = 0  # 물 안잠김

# 안전 영역 개수 구하기
# DFS
def dfs(x, y):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    if temp_array[x][y] == 1: # 방문하였거나 물 잠김
        return False

    # 방문처리
    temp_array[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 넘어가면 다음 반복문으로
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        dfs(nx, ny)
    return True

max_count = 0

for h in range(1, maxNumber+1):
    count = 0
    area(h)

    for i in range(n):
        for j in range(n):
            if dfs(i, j):
                count += 1

    # 임시 배열 초기화
    temp_array = [[0] * n for _ in range(n)]

    max_count = max(max_count, count)

print(max_count)
