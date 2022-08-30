def solution(n, m, k):
  if n == 0:
    print('z' * m)
    return
  elif m == 0:
    print('a' * n)
    return

  if dp[n - 1][m] >= k:
    print('a', end='')
    solution(n - 1, m, k)
  else:
    print('z', end='')
    solution(n, m - 1, k - dp[n - 1][m])

if __name__ == "__main__":
  n, m, k = map(int, input().split())
  dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
  for i in range(1, n + 1):
    dp[i][0] = 1
  for j in range(1, m + 1):
    dp[0][j] = 1

  for i in range(1, n + 1):
    for j in range(1, m + 1):
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

  if dp[n][m] < k:
    print(-1)
  else:
    solution(n, m, k)


# 1. 단순 순열조합으로 풀경우 n,m이 최대 100이므로 시간초과과 날것이다.
# 2. dp[i][j] ; i개의 'a'과 j개의 'z'로 만들 수 있는 문자열의 개수라고 가정할 때 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]라고 할 수 있다.
#   -> 맨 처음 'a'가 올 경우와 'z'가 올 경우를 나누어서 생각하면 됨.
# 3. dp를 초기화한다.
# 4-1. 모든 경우의 수 dp[n][m]이 k보다 작을 경우 -1을 출력한다.
# 4-2.  n이나 m이 0일 경우 경우의 수가 1이고 그 외에는 'a'가 처음에 올 경우를 기준으로 k보다 크면 'a'가 먼저, 작으면 'z'로 시작된다.
#       'z'부터 시작할 경우 k - dp[n - 1][m]을 하여 'a'가 먼저 오는 경우의 수를 제외한다.