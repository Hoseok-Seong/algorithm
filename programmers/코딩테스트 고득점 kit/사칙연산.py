def solution(arr):
    n = len(arr) // 2 + 1
    dp_max = [[0] * n for _ in range(n)]
    dp_min = [[0] * n for _ in range(n)]

    for i in range(n):
        dp_max[i][i] = dp_min[i][i] = int(arr[i * 2])

    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap
            dp_max[i][j] = float('-inf')
            dp_min[i][j] = float('inf')
            for k in range(i, j):
                if arr[k * 2 + 1] == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j])
                else:
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k + 1][j])

    return dp_max[0][n - 1]