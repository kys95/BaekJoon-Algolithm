import sys
input = sys.stdin.readline

# 게임횟수 x, 이긴횟수 y 입력
x, y = map(int, input().split())
# 승률
z = (y * 100) // x

# 승률 올릴 수 없는 경우
if z >= 99:
  print(-1)
else:
  left = 1
  right = x
  result = 0
  while left <= right:
    mid = (left + right) // 2
    # 승률 변화 없을 때
    if (y + mid) * 100 // (x + mid) <= z:
      left = mid + 1
    # 최소 횟수 찾기 위함
    else:
      result = mid
      right = mid - 1

  print(result)