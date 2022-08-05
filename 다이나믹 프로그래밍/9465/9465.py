if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0 for _ in range(n)] for _ in range(2)]
    for i in range(2):
      dp[i][0] = sticker[i][0]
      if n > 1:
        dp[i][1] = sticker[i ^ 1][0] + sticker[i][1]

    for j in range(2, n):
      for i in range(2):
        dp[i][j] = max(dp[i ^ 1][j - 2], dp[i ^ 1][j - 1]) + sticker[i][j]

    print(max(dp[0][n - 1], dp[1][n - 1]))

# 1. abc
#    efg 이렇게 있을 경우, c를 선택하면 e와 f중에서 반드시 선택해야 하고 g를 선택하면 a와 b중에서 반드시 하나를 선택해야 한다.
# 2. bottom-up방식으로 1열과 2열을 따로 처리해주고 3열 이상부터는 위의 점화식대로 처리해준다.
# 3. 최종적으로 0행 n열과 1행 n열의 최댓값을 출력한다.