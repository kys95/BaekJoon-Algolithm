from bisect import bisect_left
# 수열크기n입력
n = int(input())
# 수열입력
data = list(map(int, input().split()))
# dp테이블
dp = [data[0]]
for i in range(1, n):
    # 증가한다면
    if data[i] > dp[-1]:
        dp.append(data[i])
    else:
        index = bisect_left(dp, data[i])
        dp[index] = data[i]
print(len(dp))