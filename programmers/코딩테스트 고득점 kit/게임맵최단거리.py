from collections import deque

def solution(maps):

    # 동서남북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    visited = [[False] * len(maps[0]) for _ in range(len(maps))]

    queue = deque()

    queue.append((0, 0, 1))

    visited[0][0] = True

    answer = []

    while queue:

        x, y, distance = queue.popleft()

        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            answer.append(distance)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny, distance+1))

    if len(answer) == 0:
        return -1
    else:
        return min(answer)
