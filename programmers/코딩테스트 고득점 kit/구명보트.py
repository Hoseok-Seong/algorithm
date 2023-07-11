from collections import deque

def solution(people, limit):

    my_list = sorted(people, reverse = True)

    queue = deque(my_list)

    count = 0

    while queue:
        if queue[0] + queue[-1] <= limit and len(queue) >= 2:
            queue.popleft()
            queue.pop()
            count += 1
        else:
            queue.popleft()
            count += 1

    return count