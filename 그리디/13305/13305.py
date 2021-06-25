import sys
input = sys.stdin.readline

# 도시 갯수 n 입력
n = int(input().rstrip())
# 도시 간 거리 입력
roads = list(map(int, input().split()))
# 주유소의 리터당 가격
costs = list(map(int, input().split()))
# 최종 출력할 최소 비용
result = 0
# 현재 가격
current = costs[0]

# 가격 비교
for i in range(n - 1):
  if current > costs[i]:
    current = costs[i]
  result += roads[i] * current

print(result)