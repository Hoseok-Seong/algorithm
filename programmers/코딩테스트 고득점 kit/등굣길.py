def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[1][1] = 1

    for x, y in puddles:
        dp[x][y] = -1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dp[i][j] == -1:  # 웅덩이인 경우
                dp[i][j] = 0
            else:
                if i != 1:
                    dp[i][j] += dp[i-1][j]
                if j != 1:
                    dp[i][j] += dp[i][j-1]
                dp[i][j] %= MOD

    return dp[m][n]