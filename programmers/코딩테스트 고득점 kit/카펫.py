def solution(brown, yellow):
    num = brown + yellow

    answer = []

    for i in reversed(range(1, num+1)):
        if num % i == 0:
            if ((num // i) * 2) + ((i - 2) * 2) == brown:
                answer.append(i)
                if i * i == num:
                    answer.append(i)

    return answer