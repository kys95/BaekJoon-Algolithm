# 1.물고기 graph 정보입력
# 2.상어 물고기 잡아먹음
# 3.물고기이동
# 4.상어 이동리스트 구함
# 5.반복

import sys

input = sys.stdin.readline
from copy import deepcopy


def moveShark(fish, x, y):
    cases = []
    dir = fish[x][y][1]

    for i in range(1, 4):  # 최대 3번이동 가능
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= fish[nx][ny][0] <= 16:
            cases.append((nx, ny))

        x, y = nx, ny

    return cases


def findFish(fish, index):
    for i in range(4):
        for j in range(4):
            if fish[i][j][0] == index:
                return (i, j)

    return None


def moveFish(fish, sharkX, sharkY):
    for i in range(1, 17):  # 물고기 번호순서대로

        pos = findFish(fish, i)  # 물고기 위치 확인

        if pos == None:  # 물고기가 먹혔다면 다음 물고기 이동
            continue

        x, y = pos[0], pos[1]  # i번 물고기 좌표
        dir = fish[x][y][1]  # i번 물고기 방향

        for _ in range(8):  # 물고기당 최대 8번 방향 확인
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < 4 and 0 <= ny < 4:

                if not (nx == sharkX and ny == sharkY):  # 상어 위치 아니라면 물고기 위치교환

                    fish[x][y][0], fish[nx][ny][0] = fish[nx][ny][0], fish[x][y][0]
                    fish[x][y][1], fish[nx][ny][1] = fish[nx][ny][1], dir

                    break

            dir = (dir + 1) % 8  # 물고기 방향 45도 전환


def dfs(fishes, x, y, total):
    global result

    fish = deepcopy(fishes)

    total += fish[x][y][0]  # 상어가 물고기 잡아먹음
    fish[x][y][0] = -1

    moveFish(fish, x, y)  # 물고기 이동(매개변수로 상어 좌표)
    cases = moveShark(fish, x, y)  # 상어가 이동할 수 있는 모든 경우의 수

    result = max(result, total)
    for nextX, nextY in cases:
        dfs(fish, nextX, nextY, total)


if __name__ == "__main__":

    data = [list(map(int, input().split())) for _ in range(4)]
    fishes = [[0] * 4 for _ in range(4)]

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    # 물고기정보 리스트에 [물고기번호, 물고기방향]
    for i in range(4):
        for j in range(4):
            fishes[i][j] = [data[i][j * 2], data[i][j * 2 + 1] - 1]

    result = 0
    dfs(fishes, 0, 0, 0)
    print(result)