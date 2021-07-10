import heapq
import sys
input = sys.stdin.readline

# 강의갯수 n입력
n = int(input().rstrip())
# 시작시간, 끝나는시간 정보담을 리스트
classes = []
# 강의번호, 시작시간, 끝나는시간 입력
for _ in range(n):
  idx, start, end = map(int, input().split())
  classes.append((start, end))

def solution():
  # 시작시간 기준 정렬
  classes.sort(key= lambda x:x[0])
  # 우선순위 큐
  heap = []
  # 시작시간 가장 빠른 강의 heap에 (끝나는시간, 시작시간)삽입
  heapq.heappush(heap, (classes[0][1], classes[0][0]))
  # 강의실 갯수
  room = 1
  for i in range(1, n):
    # 현재 강의 시작시간, 끝나는시간
    now_start = classes[i][0]
    now_end = classes[i][1]
    # 이전 강의 끝나는시간, 시작시간
    be_end, be_start = heapq.heappop(heap)
    # 같은 강의실 사용 x
    if now_start < be_end:
      heapq.heappush(heap, (be_end, be_start))
      room += 1       # 강의실 추가
    heapq.heappush(heap, (now_end, now_start))

  print(room)

if __name__ == '__main__':
  solution()