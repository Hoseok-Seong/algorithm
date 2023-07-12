from collections import defaultdict, deque

def solution(tickets):
    # 그래프 생성
    graph = defaultdict(list)
    for ticket in tickets:
        departure, arrival = ticket
        graph[departure].append(arrival)

    # 그래프 정렬
    for key in graph:
        graph[key].sort()

    # BFS 탐색
    answer = []
    stack = ["ICN"]
    while stack:
        current = stack[-1]
        if current not in graph or len(graph[current]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(graph[current].pop(0))

    # 경로를 반대로 저장했으므로 역순으로 반환
    return answer[::-1]
