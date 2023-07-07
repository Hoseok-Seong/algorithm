from collections import deque

def solution(begin, target, words):

    if target not in words:
        return 0

    queue = deque()

    visited = [0] * len(words)

    queue.append((begin, 0))

    while queue:
        to_word, step = queue.popleft()

        if to_word == target:
            return step

        for i, from_word in enumerate(words):
            if visited[i] == 0 and verify(to_word, from_word):
                visited[i] == 1
                queue.append((from_word, step + 1))

    return 0

def verify(word1, word2):
    count = sum(w1 != w2 for w1, w2 in zip(word1, word2))
    return count == 1