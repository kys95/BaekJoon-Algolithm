from itertools import combinations

n, m = map(int, input().split())
# 바이러스, 빈칸 좌표담을 리스트
virus = []
blank = []
# 정보담을 그래프, 3개 추가할 temp
graph = []
temp = [[0] * m for _ in range(n)]
# 4가지 방향 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 결과
result = 0

for i in range(n):
  data = list(map(int, input().split()))
  for j in range(m):
    if data[j] == 2:
      virus.append((i, j))
    elif data[j] == 0:
      blank.append((i, j))
  graph.append(data)
# 바이러스 퍼뜨리기
def spread_virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      if temp[nx][ny] == 0:
        temp[nx][ny] = 2
        spread_virus(nx, ny)   
# 안전 영역 크기 계산
def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1 
  return score

# 조합의 수
choices = list(combinations(blank, 3))
for choice in choices:
  # 벽 설치
  for x, y in choice:
    graph[x][y] = 1
  # 그래프 정보 입력  
  for i in range(n):
    for j in range(m):
      temp[i][j] = graph[i][j]
  # 바이러스 전파
  for x, y in virus:
    spread_virus(x, y)
  # 안전 영역의 최댓값 계산
  result = max(result, get_score())
  # 리셋
  for x, y in choice:
    graph[x][y] = 0

print(result)
