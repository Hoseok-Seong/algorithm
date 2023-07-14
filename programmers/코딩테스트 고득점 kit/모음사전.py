def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']  # 알파벳 모음 리스트
    answer = 0
    count = 1  # 단어의 순서를 나타내는 변수

    for i in range(len(word)):
        # 현재 위치의 알파벳이 알파벳 모음 리스트에서 몇 번째인지 계산하여 더해줌
        answer += vowels.index(word[i]) * ((5 ** (5 - i)) - 1) / 4

    return int(answer + len(word))
