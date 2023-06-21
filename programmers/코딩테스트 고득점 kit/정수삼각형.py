def solution(triangle):

    memo = [[0] * len(triangle[i]) for i in range(len(triangle))]

    memo[0][0] = triangle[0][0]

    for i in range(len(triangle)):
        for j in range(i):
            memo[i][j] = max(memo[i][j], memo[i-1][j] + triangle[i][j])
            memo[i][j+1] = memo[i-1][j] + triangle[i][j+1]

    return max(memo[-1])