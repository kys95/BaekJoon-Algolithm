# 1.낚시왕 한칸 오른쪽 이동 -> 상어 있으면 잡음
# 2.상어 이동 -> 상어가 같은 좌표에 위치할 때 큰 상어가 작은 상어 잡아먹음(하나의 좌표에 한 상어만)

import sys

input = sys.stdin.readline

def moveShark(shark):
    b = dict()

    for (x, y), (size, speed, dir) in shark.items():

        nx = x
        ny = y

        for _ in range(speed):
            nx += dx[dir]
            ny += dy[dir]

            if not (0 <= nx < r):
                if 0 > nx:
                    nx += 2
                    dir = 1

                else:
                    nx -= 2
                    dir = 0

            if not (0 <= ny < c):

                if 0 > ny:
                    ny += 2
                    dir = 2

                else:

                    ny -= 2
                    dir = 3

        if (nx, ny) in b:  # 이미 상어가 한칸에 겹치는 경우
            if b[(nx, ny)][0] < size:  # 큰 상어가 작은 상어 잡아먹음
                b[(nx, ny)] = (size, speed, dir)
        else:
            b[(nx, ny)] = (size, speed, dir)

    return b


# 낚시왕이 한칸 오른쪽 이동하고 같은 열에 상어가 있다면 잡음
def catchShark(shark, cnt):
    global result

    for i in range(r):
        if (i, cnt) in shark:
            result += shark[(i, cnt)][0]
            del shark[(i, cnt)]
            break

    return


if __name__ == "__main__":

    r, c, m = map(int, input().split())  # rxc, m:상어갯수
    shark = dict()  # 상어정보 담을 딕셔너리
    result = 0  # 낚시왕이 잡은 상어크기의 합

    for _ in range(m):
        x, y, speed, dir, size = map(int, input().split())  # 상어x,y좌표/속력,이동방향,크기
        shark[(x - 1, y - 1)] = [size, speed, dir - 1]  # 상어좌표:key, 크기,속력,이동방향:value

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    cnt = -1  # 낚시왕 열의 위치

    while cnt <= c:
        cnt += 1
        catchShark(shark, cnt)  # 낚시왕 오른쪽으로 한칸 이동
        shark = moveShark(shark)  # 상어 이동

    print(result)
