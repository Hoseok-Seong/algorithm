from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque(truck_weights)
    answer = 0
    bridge = deque([0] * bridge_length)
    current_weight = 0

    while queue:
        answer += 1
        current_weight -= bridge.popleft()

        if current_weight + queue[0] <= weight:
            truck = queue.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)

    answer += bridge_length
    return answer