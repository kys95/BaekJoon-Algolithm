from collections import deque
import sys
input = sys.stdin.readline

# 지도 크기 nxm, 주사위를 놓은 곳의 좌표 x, 명령의 개수 k 입력
n, m, x, y, k = map(int, input().split())
# 지도
arr = []
# 지도 정보 입력
for _ in range(n):
  arr.append(list(map(int, input().split())))
# 명령정보 입력
orders = list(map(int, input().split()))
# 주사위 가로, 세로
width = deque([0] * 4)
length = deque([0] * 4)

def solution():
  global x, y
  for order in orders:
    if order == 4:  # 남
      x += 1
      if 0 <= x < n and 0 <= y < m:
        length.rotate(1)
        width[1] = length[1]
        width[3] = length[3]
        if arr[x][y] != 0:
          length[3] = arr[x][y]; arr[x][y] = 0
        else:
          arr[x][y] = length[3]
        width[3] = length[3]
        # 주사위 윗면 출력
        print(length[1])
      else:
        x -= 1

    elif order == 3:  # 북
      x -= 1
      if 0 <= x < n and 0 <= y < m:
        length.rotate(-1)
        width[1] = length[1]
        width[3] = length[3]
        if arr[x][y] != 0:
          length[3] = arr[x][y]; arr[x][y] = 0
        else:
          arr[x][y] = length[3]
        width[3] = length[3]
        # 주사위 윗면 출력
        print(length[1])
      else:
        x += 1

    elif order == 1:    # 동
      y += 1
      if 0 <= x < n and 0 <= y < m:
        width.rotate(1)
        length[1] = width[1]
        length[3] = width[3]
        if arr[x][y] != 0:
          length[3] = arr[x][y]; arr[x][y] = 0
        else:
          arr[x][y] = length[3]
        width[3] = length[3]
        # 주사위 윗면 출력
        print(length[1])
      else:
        y -= 1

    elif order == 2:     # 서
      y -= 1
      if 0 <= x < n and 0 <= y < m:
        width.rotate(-1)
        length[1] = width[1]
        length[3] = width[3]
        if arr[x][y] != 0:
          length[3] = arr[x][y]; arr[x][y] = 0
        else:
          arr[x][y] = length[3]
        width[3] = length[3]
        # 주사위 윗면 출력
        print(length[1])
      else:
        y += 1


if __name__ =="__main__":
  solution()