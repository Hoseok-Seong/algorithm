from collections import deque

def solution(priorities, location):

    order = deque(priorities)
    cnt = 0

    my_index = [0] * len(priorities)

    my_index[location] = 1

    while True:
        if not my_index or max(my_index) == 0:
            break
        if order[0] != max(order):
            order.append(order[0])
            my_index.append(my_index[0])
            order.popleft()
            del my_index[0]
        else:
            cnt += 1
            order.popleft()
            del my_index[0]

    return cnt