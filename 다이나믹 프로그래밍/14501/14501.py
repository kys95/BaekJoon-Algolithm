# n일 입력
n = int(input())
# 걸리는 기간 t, 받는 금액 p
t = []
p = []
# t, p 정보 입력
for i in range(n):
  time, price = map(int, input().split())
  t.append(time)
  p.append(price)
# dp 테이블 초기화
dp = [0] * (n + 1)
# 최대이익
max_val = 0

# 역순으로 최대이익을 dp로 입력
for i in range(n - 1, -1, -1):
  # n일에 상담가능하다면
  if t[i] + i <= n:
    dp[i] = max(max_val, p[i] + dp[t[i] + i])
    max_val = dp[i]
  # 상담기간 벗어난다면
  else:
    dp[i] = max_val

print(max_val)
