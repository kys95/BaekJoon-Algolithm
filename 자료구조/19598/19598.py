import heapq
import sys

input = sys.stdin.readline

# 배열 크기 n입력
n = int(input().rstrip())
# 회의시간 리스트
meetings = []
# 회의시간 입력
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))
# 회의시작 시간, 끝나는 시간 순서로 오름차순 정렬
meetings.sort(key=lambda x: (x[0], x[1]))

# 최소 회의실 찾기
def solution():
    # 회의시간 저장할 힙
    heap = []
    for meeting in meetings:
        # 다음 회의를 이어서 할 수 있다면
        if heap and heap[0] <= meeting[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, meeting[1])

    # 최소 회의실 갯수 출력
    print(len(heap))

solution()