def solution(S):
    stack = []

    for char in S:
        if len(stack) >= 1 and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)
