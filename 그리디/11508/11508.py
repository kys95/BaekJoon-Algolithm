import sys
input = sys.stdin.readline

# 유제품 수 n 입력
n = int(input().rstrip())
# 유제품 가격 리스트
costs = []
# 유제품 가격 입력
for _ in range(n):
  costs.append(int(input().rstrip()))
# 내림차순 정렬
costs = sorted(costs, reverse=True)
# 무료 지불할 유제품 갯수
num = n // 3
# 무료 지불 가격
result = 0
for i in range(num):
  result += costs[3 * (i + 1) - 1]
# 무료 지불 가격을 뺀 순수 지불 금액
print(sum(costs) - result)