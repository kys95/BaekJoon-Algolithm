def re_paint(color):
    global answer
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            if i > 0 and j > 0:
                dp[i][j] -= dp[i - 1][j - 1]
            if (i + j) % 2 and board[i][j] == color:
                dp[i][j] += 1
            if (i + j) % 2 == 0 and board[i][j] != color:
                dp[i][j] += 1

    for i in range(n - 7):
        for j in range(m - 7):
            cnt = dp[i + 7][j + 7]

            if i > 0:
                cnt -= dp[i - 1][j + 7]
            if j > 0:
                cnt -= dp[i + 7][j - 1]
            if i > 0 and j > 0:
                cnt += dp[i - 1][j - 1]

            answer = min(answer, cnt)


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    answer = 64

    re_paint('B')
    re_paint('W')

    print(answer)