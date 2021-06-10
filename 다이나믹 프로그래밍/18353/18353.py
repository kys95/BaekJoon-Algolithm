# 병사 수 n입력
n = int(input())
# 각 병사의 전투력 정보 입력
data = list(map(int, input().split()))
# dp테이블 초기화
dp = [1] * n

# 내림차순으로 남아있는 최대의 병사 수 확인
for i in range(1, n):
  for j in range(i):
    # 전투력이 작다면
    if data[j] > data[i]:
      dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))