import sys
input = sys.stdin.readline

# 거스름 돈 액수 n 입력
n = int(input().rstrip())
# 1, 3은 거슬러 줄 수 없음
if n == 1 or n == 3:
  result = -1
# 5로나눈 나머지가 2로 나누어 떨어질 때
elif (n % 5) % 2 == 0:
  result = (n // 5) + (n % 5) // 2
else:
  result = (n // 5) - 1 + ((n % 5) + 5) // 2
print(result)