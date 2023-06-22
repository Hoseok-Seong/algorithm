def solution(S):
    if len(S) == 1:
        return 0

    if len(S) % 2 == 0:
        return -1

    for i in range(len(S) // 2):
        if S[i] != S[-(i+1)]:
            return -1

    return len(S) // 2

    return cnt

