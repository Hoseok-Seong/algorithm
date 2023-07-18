def solution(routes):
    routes.sort(key=lambda x: x[1])  # 차량 경로를 진출 지점을 기준으로 오름차순으로 정렬
    camera_count = 0  # 최소 카메라 개수
    current_camera = -30001  # 현재 카메라 위치를 초기화

    for route in routes:
        if route[0] > current_camera:
            # 현재 차량의 진입 지점이 현재 카메라 위치보다 크다면, 새로운 카메라가 필요
            camera_count += 1
            current_camera = route[1]  # 현재 카메라 위치를 현재 차량의 진출 지점으로 갱신

    return camera_count
