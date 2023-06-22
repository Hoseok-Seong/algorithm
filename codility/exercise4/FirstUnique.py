from collections import Counter

def solution(A):

    my_cnt = Counter(A)

    for i in my_cnt.keys():
        if my_cnt[i] == 1:
            return i

    return -1