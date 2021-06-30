import heapq
import sys
input = sys.stdin.readline

# 최소비용 출력
def solution():
  heap = []
  # 힙에 파일 크기 푸시
  for data in files:
    heapq.heappush(heap, data)
  # 최소비용
  result = 0
  # 힙에 한개 남을때 까지 반복
  while len(heap) != 1:
    # 최소 파일크기 두개 팝
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    # 파일 두개 합침
    result += (first + second)
    # 힙에 다시 푸시
    heapq.heappush(heap, first + second)

  print(result)

if __name__ == '__main__':
  # 테스트 데이터 갯수 t 입력
  t = int(input().rstrip())
  for _ in range(t):
    # 소설 챕터 갯수 k 입력
    k = int(input().rstrip())
    # k개의 파일 크기 입력
    files = list(map(int, input().split()))
    # 최소비용 출력함수
    solution()