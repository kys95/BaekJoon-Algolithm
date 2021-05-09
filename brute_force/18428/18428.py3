from itertools import combinations
# n 입력
n = int(input())
# 복도
hall = []
# 선생님, 빈칸
teachers = []
empty = []
# 복도 정보 입력
for i in range(n):
  hall.append(list(input().split()))
  for j in range(n):
    # 선생님이면
    if hall[i][j] == 'T':
      teachers.append((i, j))
    # 빈칸이면
    elif hall[i][j] == 'X':
      empty.append((i, j))
# 장애물 3개 놓는 모든 경우의 수
obstacles = list(combinations(empty, 3))

# 감시
def watch():
  # 모든 선생님의 위치 확인
  for x, y in teachers:
    # 상
    nx, ny = x, y
    while nx > 0:
      nx -= 1
      if hall[nx][ny] == 'S':
        return False
      if hall[nx][ny] == 'O':
        break 
    # 하
    nx, ny = x, y
    while nx < n - 1:
      nx += 1
      if hall[nx][ny] == 'S':
        return False
      if hall[nx][ny] == 'O':
        break 
    # 좌
    nx, ny = x, y
    while ny > 0:
      ny -= 1
      if hall[nx][ny] == 'S':
        return False
      if hall[nx][ny] == 'O':
        break 
    # 우
    nx, ny = x, y
    while ny < n - 1:
      ny += 1
      if hall[nx][ny] == 'S':
        return False
      if hall[nx][ny] == 'O':
        break 
  return True   

# 장애물 3개 놓는 경우의 수
for obstacle in obstacles:
  # 장애물 3개 설치
  for x, y in obstacle:
    hall[x][y] = 'O'
  if watch() == True:
    print('YES')
    break
  # 장애물 3개 해제
  for x, y in obstacle:
    hall[x][y] = 'X'
else:
  print('NO')
