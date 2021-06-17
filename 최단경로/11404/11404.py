import sys
input = sys.stdin.readline
INF = int(1e9)

# 도시갯수 n, 버스갯수 m입력
n = int(input())
m = int(input())
# 도시정보 담을 그래프
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 버스정보 입력
for _ in range(m):
  a, b, c = map(int, input().split())
  # 도시 a->b 가는데 드는 비용 c
  # 단, 노선이 여러개일 경우 짧은 것만
  if c < graph[a][b]:
        graph[a][b] = c

# 자기 자신으로 가는 도시 0으로 초기화
for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i == j:
      graph[i][j] = 0

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 최소비용 출력
for a in range(1, n + 1):
  for b in range(1, n + 1):
    # 도달할 수 없는 경우
    if graph[a][b] == INF:
        print(0, end=' ')
    else:
        print(graph[a][b], end=' ')
  print()