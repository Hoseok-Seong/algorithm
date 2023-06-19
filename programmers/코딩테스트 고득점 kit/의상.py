def solution(clothes):
    name = dict(clothes).keys()
    type = set(dict(clothes).values())
    type2 = list(dict(clothes).values())

    num = []

    for i in type:
        num.append(type2.count(i) + 1)

    answer = 1

    for i in range(0, len(num)):
        answer *= num[i]

    return answer - 1