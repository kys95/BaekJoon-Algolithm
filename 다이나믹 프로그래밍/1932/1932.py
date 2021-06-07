n = int(input())

dp = []
for i in range(n):
    data = list(map(int, input().split()))
    dp.append(data)

for i in range(1, n):
    for j in range(len(dp[i])):
        # 대각선 오른쪽
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        # 대각선 왼쪽
        if j == (len(dp[i]) - 1):
            up_right = 0
        else:
            up_right = dp[i - 1][j]

        dp[i][j] = dp[i][j] + max(up_left, up_right)

print(max(dp[n - 1]))