import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_list = list(numbers)
    prime_set = set()

    # 가능한 모든 숫자 조합 생성
    for i in range(1, len(num_list) + 1):
        perm = itertools.permutations(num_list, i)

        for p in perm:
            num = int(''.join(p))
            if is_prime(num):
                prime_set.add(num)

    answer = len(prime_set)
    return answer
