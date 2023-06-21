from collections import deque

def solution(n, lost, reserve):

    my_lost = set(lost) - set(reserve)

    my_reserve = set(reserve) - set(lost)

    queue = deque(my_reserve)

    cnt = 0

    for i in my_lost:
        for j in range(len(queue)):
            if i - 1 == queue[j]:
                cnt += 1
                queue.popleft()
                break
            if i + 1 == queue[j]:
                cnt += 1
                queue.popleft()
                break

    return cnt + (n-len(my_lost))