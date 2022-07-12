from collections import deque 
# N,L,R입력
N, L, R = map(int, input().split())
# 각 나라 인구 리스트
countries = []
# 각 나라 인구 입력
for _ in range(N):
  countries.append(list(map(int, input().split())))
# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# bfs알고리즘
def bfs(x, y):
  # 한번 확인할 때 연합된 나라 담을 리스트
  union = []
  union.append((x, y))
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    # 상,하,좌,우
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 조건
      if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
        if L <= abs(countries[nx][ny] - countries[x][y]) <= R:
          # 방문확인
          visited[nx][ny] = 1
          q.append((nx, ny))
          union.append((nx, ny))
  # 연합되는 나라가 2개 이상일 경우
  if len(union) >= 2:
    union_list.append(union)

# 인구 이동
def move_people(union_list):
  for union in union_list:
    total = 0
    for x, y in union:
      total += countries[x][y]
    for x, y in union:
      countries[x][y] = total // len(union)
    
# 최종 인구 이동 횟수
count = 0
while True:
  # 하루동안 연합되는 연합리스트
  union_list = []
  # 방문 리스트
  visited = [[-1] * N for _ in range(N)]
  # 모든 나라 확인
  for i in range(N):
    for j in range(N):
      if visited[i][j] == -1:
        # 방문 확인
        visited[i][j] = 1
        bfs(i, j)
  # 연합되는 나라가 있는 경우
  if union_list:
    move_people(union_list)
    count += 1
  else:
    break
print(count)