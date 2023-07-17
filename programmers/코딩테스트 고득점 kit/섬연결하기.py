def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def solution(n, costs):
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    # 비용을 기준으로 간선들을 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    answer = 0
    for u, v, cost in costs:
        # 두 섬이 같은 집합에 속해 있지 않으면 연결
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            answer += cost

    return answer