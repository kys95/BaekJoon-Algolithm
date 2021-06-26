import sys

input = sys.stdin.readline
import heapq

# 회의실 갯수 n 입력
n = int(input().rstrip())
heap = []
# 회의실 시작, 끝 시간 입력
for _ in range(n):
    start, end = map(int, input().split())
    heapq.heappush(heap, (end, start))

count = 1
now_end, now_start = heapq.heappop(heap)
while heap:
    next_end, next_start = heapq.heappop(heap)
    if next_start >= now_end:
        now_end = next_end
        count += 1

print(count)