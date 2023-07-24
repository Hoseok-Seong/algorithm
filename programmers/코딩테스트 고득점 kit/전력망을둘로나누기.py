def solution(n, wires):
    def dfs(node, parent):
        count = 1
        for neighbor in graph[node]:
            if neighbor != parent:
                count += dfs(neighbor, node)
        return count

    graph = {i: [] for i in range(1, n + 1)}
    for wire in wires:
        v1, v2 = wire
        graph[v1].append(v2)
        graph[v2].append(v1)

    min_difference = float('inf')
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        count1 = dfs(v1, v2)
        count2 = n - count1
        min_difference = min(min_difference, abs(count1 - count2))

        graph[v1].append(v2)
        graph[v2].append(v1)

    return min_difference
