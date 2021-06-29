import heapq
import sys
input = sys.stdin.readline

# 수업 갯수 n 입력
n = int(input().rstrip())
# 수업시간 담을 리스트
classes = []
# 시작시간, 끝나는 시간 입력
for _ in range(n):
  start, end = map(int, input().split())
  classes.append((start, end))

# 시작시간, 끝나는시간 순으로 오름차순 정렬
classes.sort(key=lambda x:(x[0], x[1]))

# 최소 강의실 갯수
def solution():
  heap = []
  for start, end in classes:
    if heap and heap[0] <= start:
      heapq.heappop(heap)
    heapq.heappush(heap, end)

  print(len(heap))

if __name__ == '__main__':
  solution()