import sys
input = sys.stdin.readline

# 정수 a, b 입력
a, b = map(int, input().split())

# 최소 연산 횟수
count = 0

while a < b:
  # b의 끝자리가 1일 경우
  if b % 10 == 1:
    b //= 10
  # b가 2로 나누어 떨어질 경우
  elif b % 2 == 0:
    b //= 2
  else:
    break
  count += 1

# a -> b로 바꿀수 있다면
if a == b:
  print(count + 1)
else:
  print(-1)