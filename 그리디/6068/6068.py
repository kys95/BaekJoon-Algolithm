import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 일의 갯수 n 입력
n = int(input().rstrip())
# 우선순위 큐
heap = []
# 일이 걸리는 시간, 최소 마감시간 입력
for _ in range(n):
    cost, end = map(int, input().split())
    # 최소마감 시간 최대힙
    heapq.heappush(heap, (-end, cost))

def solution():
    # 다음 해야할 일의 시작 시간
    af_start_time = INF
    while heap:
        # 마감시간, 걸리는 시간
        end_time, cost = heapq.heappop(heap)
        end_time = - end_time  # 본래의 끝나는 시간

        # 현재 일의 끝나는 시간이 다음 일의 시작시간보다 느리다면 끝나는시간을 앞당김
        if end_time > af_start_time:
            end_time = af_start_time
        af_start_time = end_time - cost  # 시작 시간

    if af_start_time >= 0:
        print(af_start_time)
    else:
        print(-1)

if __name__ == '__main__':
    solution()