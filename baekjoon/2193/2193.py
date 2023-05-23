n = int(input())

def dp(n):
    dp = [0] * (n+1)
    dp[1] = 1 # 1

    if n >= 2:
        dp[2] = 1 # 10

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

result = dp(n)

print(result)