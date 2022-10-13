n, m, k = map(int, input().split())

# 처음상어 위치
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


shark = [[0,0] for _ in range(m)]

# 상어의 초기 방향 정해주기
directions = list(map(int, input().split()))

# 상어의 방향별 우선순위 받아오기(위 아래 왼쪽 오른쪽)
priorities = []
for i in range(m):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    priorities.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상황판 그리기(상어번호, 냄새가 머무는 시간, 방향)
smell = [[[0, 0]] * n for _ in range(n)]

# 모든 냄새 정보 업데이트
def update_smell():
    for i in range(n):
        for j in range(n):
            # 냄새가 남아있는 경우
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어가 존재하는 위치의 경우
            if data[i][j] != 0:
                smell[i][j] = [data[i][j], k]


# 상어 이동
def move():
    new_data = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if data[x][y] != 0:
                direction = directions[data[x][y] - 1]
                found = False
                # 상어의 위치인 경우
                for idx in priorities[data[x][y] - 1][direction - 1]:
                    nx = x + dx[idx - 1]
                    ny = y + dy[idx - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0: # 냄새가 나지 않는 곳이라면
                            directions[data[x][y] - 1] = idx
                            # 상어 이동시키기
                            if new_data[nx][ny] == 0:
                                new_data[nx][ny] = data[x][y]
                            else :
                                new_data[nx][ny] = min(data[x][y], new_data[nx][ny])
                            found = True
                            break
                if found:
                    continue

                # 주변에 모두 냄새가 남아있다면, 자신의 냄새가 있는 곳으로 이동
                for idx in priorities[data[x][y] - 1][direction - 1]:
                    nx = x + dx[idx - 1]
                    ny = y + dy[idx - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == data[x][y]: # 자신의 냄새가 있는 곳이라면
                            # 해당 상어 방향 변경
                            directions[data[x][y] - 1] = idx
                            # 상어 이동시키기
                            new_data[nx][ny] = data[x][y]
                            break
    return new_data

answer = 0
while True:
    update_smell()
    new_data = move()
    data = new_data
    answer += 1

    check = True
    for i in range(n):
        for j in range(n):
            if data[i][j] > 1:
                check = False
    if check:
        print(answer)
        break

    # 1000초가 지날 때까지 끝나지 않았다면
    if answer >= 1000:
        print(-1)
        break

# import sys
#
# input = sys.stdin.readline
# dx = [0, -1, 1, 0, 0]
# dy = [0, 0, 0, -1, 1]
#
# n, m, k = map(int, input().split())
#
# a, shark = [], [[] for _ in range(m)]
# for i in range(n):
#     a.append(list(map(int, input().split())))
#     for j in range(n):
#         if a[i][j]:
#             shark[a[i][j]-1].extend([i, j])
#             a[i][j] = [a[i][j], k]
#
# d = list(map(int, input().split()))
# for i in range(m):
#     shark[i].append(d[i])
#
# dir = [[] for _ in range(m)]
# idx = -1
# for i in range(4*m):
#     if i % 4 == 0:
#         idx += 1
#     dir[idx].append(list(map(int, input().split())))
#
# ans = 0
# while True:
#     ans += 1
#     if ans == 1001:
#         print(-1)
#         break
#
#     check = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(m):
#         if shark[i] != 0:
#             x, y, d, flag = shark[i][0], shark[i][1], shark[i][2], 0
#             for j in range(4):
#                 ndir = dir[i][d-1][j]
#                 nx, ny = x + dx[ndir], y + dy[ndir]
#                 if 0 <= nx < n and 0 <= ny < n:
#                     if a[nx][ny] == 0:
#                         flag = 1
#                         break
#             if flag == 0:
#                 for j in range(4):
#                     ndir = dir[i][d-1][j]
#                     nx, ny = x + dx[ndir], y + dy[ndir]
#                     if 0 <= nx < n and 0 <= ny < n:
#                         if a[nx][ny][0] == i+1:
#                             break
#
#             if check[nx][ny]:
#                 if check[nx][ny] < i+1:
#                     shark[i] = 0
#                 else:
#                     shark[check[nx][ny]-1] = 0
#             else:
#                 check[nx][ny] = i+1
#                 shark[i] = [nx, ny, ndir]
#
#     for i in range(n):
#         for j in range(n):
#             if a[i][j]:
#                 a[i][j][1] -= 1
#                 if a[i][j][1] == 0:
#                     a[i][j] = 0
#
#     for i in range(m):
#         if shark[i]:
#             x, y = shark[i][0], shark[i][1]
#             a[x][y] = [i+1, k]
#
#     if shark.count(0) == m-1:
#         print(ans)
#         break

