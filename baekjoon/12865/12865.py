n, m = map(int, input().split())
product = [list(map(int, input().split())) for _ in range(n)]

# 가치 계산하기
values = [0] * n

# 무게 계산하기
weights = [0] * n

# 가치 값 초기화
for i in range(n):
    weights[i] = product[i][0]
    values[i] = product[i][1]

# dp
def dp(n, m, weights, values):
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        weight = weights[i-1]
        value = values[i-1]

        for j in range(1, m+1):
            if weight > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

    return dp[n][m]

result = dp(n, m, weights, values)
print(result)