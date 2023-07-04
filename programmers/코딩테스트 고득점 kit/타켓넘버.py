def solution(numbers, target):
    def dfs(idx, current_sum):
        nonlocal answer
        if idx == len(numbers):  # 모든 숫자를 확인한 경우
            if current_sum == target:  # 타겟 넘버와 일치하는 경우
                answer += 1
            return

        # 현재 인덱스의 숫자를 더하거나 뺀 뒤 다음 인덱스로 재귀 호출
        dfs(idx + 1, current_sum + numbers[idx])
        dfs(idx + 1, current_sum - numbers[idx])

    answer = 0
    dfs(0, 0)

    return answer
