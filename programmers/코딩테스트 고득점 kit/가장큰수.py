def solution(numbers):

    my_list = list(map(str, numbers))

    # 문자열을 정렬하면 0부터 9 순으로 정렬된다.
    # x를 4번 반복한 후, 1부터 4까지의 숫자를 비교해서 정렬(원소는 1000 이하이므로)
    my_list.sort(key=lambda x: (x * 4) [:4], reverse=True)

    answer = ''.join(my_list)

    # 0이 답일 경우, 0이 하나만 나와야지 테스트 통과됨
    # 00, 000, 0000 등은 오답 처리됨
    if answer[0] == '0':
        return '0'
    else:
        return answer