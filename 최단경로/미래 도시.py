# 플로이드 워셜
if __name__ == "__main__":
  n, m = map(int, input().split())
  INF = int(1e9)
  graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
  for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
  x, k = map(int, input().split())

  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if i == j:
        graph[i][j] = 0

  for c in range(1, n + 1):
    for a in range(1, n + 1):
      for b in range(1, n + 1):
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

  dist = graph[1][k] + graph[k][x]

  if dist >= INF:
    print("-1")
  else:
    print(dist)