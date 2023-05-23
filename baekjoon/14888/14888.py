import sys
import itertools

input = sys.stdin.readline

n = int(input())

# 숫자
number = list(map(int, input().split()))

# 연산자 카운트
operator = list(map(int, input().split()))

result = []

real_operator = []


# 연산자로 바꿔주는 함수
def pick_operator(operator):
    if operator[0] != 0:
        for i in range(operator[0]):
            real_operator.append("+")
    if operator[1] != 0:
        for i in range(operator[1]):
            real_operator.append("-")
    if operator[2] != 0:
        for i in range(operator[2]):
            real_operator.append("*")
    if operator[3] != 0:
        for i in range(operator[3]):
            real_operator.append("/")


pick_operator(operator)


# 계산하는 함수
def calculate(number, op):
    result = number[0]
    for i in range(1, len((number))):
        if op[i - 1] == '+':
            result += number[i]
        elif op[i - 1] == '-':
            result -= number[i]
        elif op[i - 1] == '*':
            result *= number[i]
        elif op[i - 1] == '/':
            if result < 0:
                result = -((-result) // number[i])
            else:
                result //= number[i]
    return result


# 최댓값, 최솟값 만들어주는 함수
def solution(number, real_operator):
    max_result = -sys.maxsize - 1
    min_result = sys.maxsize

    # 연산자 순열
    operator_permutation = itertools.permutations(real_operator)

    for op in operator_permutation:
        result = calculate(number, op)
        min_result = min(min_result, result)
        max_result = max(max_result, result)

    return max_result, min_result


# 문제 해결 및 결과 출력
max_result, min_result = solution(number, real_operator)
print(max_result)
print(min_result)
