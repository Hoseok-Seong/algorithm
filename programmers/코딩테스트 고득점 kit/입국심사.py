def solution(n, times):
    start = 1
    end = max(times) * n

    answer = 0

    while start <= end:
        mid = (start + end) // 2

        count = 0
        for time in times:
            count += mid // time

        if count >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer