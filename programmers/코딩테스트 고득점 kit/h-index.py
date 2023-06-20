def solution(citations):
    n = len(citations)
    citations.sort()  # 인용 횟수를 오름차순으로 정렬

    h_index = 0
    for i in range(n):
        if citations[i] >= n - i:  # 현재 인용 횟수가 남은 논문 수와 같거나 큰 경우
            h_index = n - i  # H-Index 갱신
            break

    return h_index