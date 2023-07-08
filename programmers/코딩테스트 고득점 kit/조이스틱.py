def solution(name):
    name = list(name)  # 문자열을 리스트로 변환
    count = 0  # 조작 횟수
    idx = 0  # 커서 위치

    while True:
        # 현재 위치의 알파벳을 조작하여 바꾸는 횟수 계산
        count += min(ord(name[idx]) - ord('A'), ord('Z') - ord(name[idx]) + 1)
        name[idx] = 'A'  # 현재 위치의 알파벳을 'A'로 변경

        if all(char == 'A' for char in name):  # 모든 알파벳이 'A'인 경우 종료
            break

        left = 1  # 왼쪽으로 이동할 거리
        right = 1  # 오른쪽으로 이동할 거리

        # 왼쪽으로 이동할 거리 계산
        while name[(idx - left) % len(name)] == 'A':
            left += 1

        # 오른쪽으로 이동할 거리 계산
        while name[(idx + right) % len(name)] == 'A':
            right += 1

        # 커서 이동 및 조작 횟수 추가
        if left < right:
            idx = (idx - left) % len(name)
            count += left
        else:
            idx = (idx + right) % len(name)
            count += right

    return count
