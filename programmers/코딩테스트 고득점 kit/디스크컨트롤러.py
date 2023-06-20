import heapq

def solution(jobs):
    answer = 0
    start_time = 0
    end_time = 0
    jobs.sort()
    my_len = len(jobs)

    heap = []

    while jobs or heap:
        while jobs and jobs[0][0] <= end_time:
            request_time, duration = jobs.pop(0)
            heapq.heappush(heap, (duration, request_time))

        if heap:
            duration, request_time = heapq.heappop(heap)
            start_time = end_time
            end_time += duration
            answer += end_time - request_time

        else:
            end_time = jobs[0][0]

    return answer // my_len
