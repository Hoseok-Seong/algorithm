import itertools

a = list(map(int, input().split()))
b = list(map(int, input().split()))

combinations = itertools.combinations(b, 3)
answer=[]

for c in combinations:
    temp = 0
    for n in range(3):
        temp += c[n]
    answer.append(temp)

answer2=[]

for n in answer:
    if n <= a[1]:
        answer2.append(n)

print(max(answer2))