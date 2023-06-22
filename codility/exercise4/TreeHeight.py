from extratypes import Tree  # library with types used in the task

def solution(T):
    def calculate_height(T):
        if T is None:
            return -1
        else:
            left_height = calculate_height(T.l)
            right_height = calculate_height(T.r)
            return max(left_height, right_height) + 1

    return calculate_height(T)