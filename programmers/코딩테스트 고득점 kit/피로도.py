from itertools import permutations

def solution(k, dungeons):

    order = list(permutations(dungeons))

    answer = []

    hp = k

    for i in order:
        count = 0
        for j in range(len(i)):
            if hp >= i[j][0]:
                count += 1
                hp -= i[j][1]
            else:
                continue
        answer.append(count)
        hp = k

    return max(answer)