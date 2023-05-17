import itertools

a = int(input())
b = list(map(int, input().split()))

permutations = itertools.permutations(b)

answer = []

for p in permutations:
    temp_sum = 0
    for n in range(1, a):
        ans = abs(p[n-1] - p[n])
        temp_sum += ans
    answer.append(temp_sum)

max_sum = max(answer)
print(max_sum)
