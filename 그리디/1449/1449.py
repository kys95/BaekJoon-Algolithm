import sys
input = sys.stdin.readline

# 물이 새는 곳의 갯수 N, 테이프의 길이 L 입력
N, L = map(int, input().split())
# 물이 새는 곳의 위치 입력
arr = list(map(int, input().split()))

def solution(L):
  # 물이 새는 곳 오름차순 정렬
  arr.sort()
  # 테이프가 닿을 수 있는 지점
  tape = arr[0] - 0.5 + L
  # 테이프 갯수
  count = 1
  # 새는 곳 확인
  for i in range(1, len(arr)):
    # 테이프가 닿을 수 없는경우
    if tape < arr[i] + 0.5:
      # 테이프가 닿는 지점 갱신
      tape = arr[i] - 0.5 + L
      count += 1
  print(count)

if __name__ == '__main__':
  solution(L)