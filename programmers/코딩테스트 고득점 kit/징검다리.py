def solution(distance, rocks, n):
    rocks.sort()  # 바위들을 오름차순으로 정렬
    start = 0  # 최소 거리의 시작점
    end = distance  # 최소 거리의 끝점
    answer = 0

    while start <= end:
        mid = (start + end) // 2  # 중간 거리 계산
        removed_rocks = 0  # 제거한 바위 개수
        prev_rock = 0  # 이전 바위의 위치
        min_distance = float('inf')  # 각 지점 사이의 최소 거리

        for rock in rocks:
            if rock - prev_rock < mid:
                removed_rocks += 1  # 바위 제거
            else:
                min_distance = min(min_distance, rock - prev_rock)  # 최소 거리 갱신
                prev_rock = rock

        if distance - prev_rock < mid:
            removed_rocks += 1  # 마지막 바위 제거

        if removed_rocks > n:
            end = mid - 1
        else:
            answer = min_distance
            start = mid + 1

    return answer
