import heapq
# n, k 입력
n, k = map(int, input().split())
# 그래프와 우선순위 큐 
graph = []
q = []

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    # 바이러스일 때
    if graph[i][j] != 0:
      # 순서, 바이러스 종류, x좌표, y좌표  
      heapq.heappush(q,(0, graph[i][j], i, j))

# s, x, y입력
s, fx, fy = map(int, input().split())   
# 상하좌우 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
  order, virus, x, y = heapq.heappop(q)
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 범위 설정
    if nx >= 0 and nx < n and ny >= 0 and ny < n:
      # 바이러스 증식
      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y]
        heapq.heappush(q, (order + 1, virus, nx, ny))
  # 시간 초과될 때
  if order + 1 >= s:
    break

print(graph[fx - 1][fy - 1])
