import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

if __name__ == "__main__":
  n,m = map(int, input().split())
  adj = [[False for _ in range(n + 1)] for _ in range(n + 1)]
  for _ in range(m):
    a, b = map(int, input().split())
    adj[a][b] = True
    adj[b][a] = True

  ans = 0
  chk = [False] * (n + 1)

  def dfs(i):
    for j in range(1, n + 1):
      if adj[i][j] and not chk[j]:
        chk[j] = True
        dfs(j)

  for i in range(1, n + 1):
    if not chk[i]:
      ans += 1
      chk[i] = True
      dfs(i)

  print(ans)