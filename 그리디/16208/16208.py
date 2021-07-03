import sys
input = sys.stdin.readline

# 쇠막대의 수 n 입력
n = int(input().rstrip())
# 쇠막대의 길이 입력
sticks = list(map(int, input().split()))

def solution():
  # 쇠막대의 길의 합, 최소 비용
  length = sum(sticks)
  cost = 0

  # n개가 될때 까지 쇠막대 나누기
  for i in range(len(sticks) - 1):
    length -= sticks[i]
    cost += length * sticks[i]
  # 최소비용 출력
  print(cost)

if __name__ == '__main__':
  solution()