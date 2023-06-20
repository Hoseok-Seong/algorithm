# 1번: 12345 반복
# 2번: 21232425 반복
# 3번: 3311224455 반복
from collections import deque

def solution(answers):

    stu_1 = [1, 2, 3, 4, 5]
    stu_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer = []

    # 1번 수포자 풀이

    index = 0
    cnt = 0

    for i in range(len(answers)):
        if answers[i] == stu_1[index]:
            cnt += 1
        index = (index + 1) % len(stu_1)

    answer.append(cnt)

    # 2번 수포자 풀이

    index = 0
    cnt = 0

    for i in range(len(answers)):
        if answers[i] == stu_2[index]:
            cnt += 1
        index = (index + 1) % len(stu_2)

    answer.append(cnt)

    # 3번 수포자 풀이

    index = 0
    cnt = 0

    for i in range(len(answers)):
        if answers[i] == stu_3[index]:
            cnt += 1
        index = (index + 1) % len(stu_3)

    answer.append(cnt)

    # 최대 정답자 배열에 담기

    real_answer = []

    for i in range(len(answer)):
        if answer[i] == max(answer):
            real_answer.append(i+1)

    return real_answer