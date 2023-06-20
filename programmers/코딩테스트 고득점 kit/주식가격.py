from collections import deque

def solution(prices):

    queue = deque(prices)

    answer = [0] * len(prices)

    order = 0

    while queue:
        if len(queue) == 1:
            break
        cnt = 0
        for i in range(1, len(queue)):
            if queue[0] <= queue[i]:
                cnt += 1
            else:
                cnt += 1
                break
        answer[order] = cnt
        queue.popleft()
        order += 1

    return answer