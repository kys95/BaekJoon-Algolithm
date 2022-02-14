# import sys
# input = sys.stdin.readline

# def dfs(x, y, state):

#   global answer

#   if x == n - 1 and y == n - 1: #목적지 도달
#     answer += 1
#     return

#   if x + 1 < n and y + 1 < n:   #가로,세로,대각선 -> 대각선으로 이동
#     if graph[x + 1][y + 1] == 0 and graph[x + 1][y] == 0 and graph[x][y + 1] == 0:
#       dfs(x + 1, y + 1, 2)  #대각선 이동

#   if state == 0 or state == 2:  #가로,대각선 -> 가로로 이동
#     if y + 1 < n:
#       if graph[x][y + 1] == 0:
#         dfs(x, y + 1, 0)

#   if state == 1 or state == 2:  #세로, 대각선 -> 세로로 이동
#     if x + 1 < n:
#       if graph[x + 1][y] == 0:
#         dfs(x + 1, y, 1)

# if __name__ == "__main__":

#   n = int(input())
#   graph = []
#   for _ in range(n):
#     graph.append(list(map(int, input().split())))
#   answer = 0
#   dfs(0, 1, 0)

#   print(answer)

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]  # 가로,세로,대각선 각각의 경우의 수

    dp[0][0][1] = 1  # 가로,(0,1)

    for i in range(2, n):  # 첫 째줄 초기화
        if graph[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]

    for i in range(1, n):
        for j in range(2, n):

            if graph[i][j] == 0 and graph[i - 1][j] == 0 and graph[i][j - 1] == 0:  # 대각선이 오는 경우
                dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]

            if graph[i][j] == 0:
                dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]  # 가로가 오는 경우
                dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

    result = 0
    for i in range(3):
        result += dp[i][n - 1][n - 1]
    print(result)