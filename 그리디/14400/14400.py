import sys
input = sys.stdin.readline

# 거리합 최소
def solution(n):
  # x좌표, y좌표 정렬
  arr_x.sort()
  arr_y.sort()
  # 편의점 위치
  target_x = arr_x[n // 2]
  target_y = arr_y[n // 2]
  # 최종 거리
  result = 0
  for x in arr_x:
    result += abs(target_x - x)
  for y in arr_y:
    result += abs(target_y - y)

  print(result)

if __name__ == '__main__':
  # 고객 수 n 입력
  n = int(input().rstrip())
  # 고객 위치 담을 리스트
  arr_x = []
  arr_y = []
  # n개의 고객위치 입력
  for _ in range(n):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)
  solution(n)