def solution(money):
    n = len(money)
    dp1 = [0] * n  # 첫 번째 집을 털었을 때의 최대 금액
    dp2 = [0] * n  # 첫 번째 집을 털지 않았을 때의 최대 금액

    # 첫 번째 집을 털었을 때의 최대 금액 계산
    dp1[0] = money[0]
    dp1[1] = money[0]

    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # 첫 번째 집을 털지 않았을 때의 최대 금액 계산
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    # 첫 번째 집을 털었을 때와 털지 않았을 때 중 최댓값 반환
    return max(dp1[-2], dp2[-1])

