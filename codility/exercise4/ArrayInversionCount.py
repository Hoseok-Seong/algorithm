def solution(A):
    # 병합 정렬과 인버전 개수 계산을 위한 보조 함수
    def merge_sort_and_count(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, count_left = merge_sort_and_count(arr[:mid])
        right, count_right = merge_sort_and_count(arr[mid:])
        merged, count = merge_and_count(left, right)

        return merged, count + count_left + count_right

    # 병합과 인버전 개수 계산을 위한 보조 함수
    def merge_and_count(left, right):
        merged = []
        count = 0
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                count += len(left) - i  # 인버전 개수 계산
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, count

    # 병합 정렬과 인버전 개수 계산 수행
    sorted_A, inversions = merge_sort_and_count(A)

    # 인버전 개수가 1,000,000,000을 초과하는 경우 -1 반환
    if inversions > 1000000000:
        return -1

    return inversions
