# 1.말의 번호에 따라 순서대로 움직임
# 2.말이 이동하려는 좌표의 색상에 따라 말의 위치가 달라짐
# 3.말이 쌓이는 순서가 다름

import sys

input = sys.stdin.readline


def moveHorse():
    turn = 0

    while turn < 1000:  # 턴이 1000보다 크면 종료
        turn += 1

        for i in range(1, k + 1):  # 말의 번호에 따라 이동
            x, y, d = horse[i]  # 말의 번호에 따른 좌표값과 방향

            nx = x + dx[d]  # 말이 이동하려는 위치
            ny = y + dy[d]

            state = 0

            # 말이 체스판을 벗어났거나 파란색인 경우
            if 0 > nx or 0 > ny or nx >= n or ny >= n or graph[nx][ny] == Blue:
                nd = revDir[d]  # 이동 방향 반대
                nx = x + dx[nd]
                ny = y + dy[nd]

                # 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
                if 0 > nx or 0 > ny or nx >= n or ny >= n or graph[nx][ny] == Blue:
                    horse[i][2] = nd
                    continue

                state = 1

            # 이동하려는 칸이 흰색인 경우
            if graph[nx][ny] == White:
                down = graph_2[(x, y)][:graph_2[(x, y)].index(i)]  # 해당말의 아래에 있는 말들
                up = graph_2[(x, y)][graph_2[(x, y)].index(i):]  # 해당말을 포함한 위에 있는 말들
                graph_2[(x, y)] = down

                graph_2[(nx, ny)].extend(up)  # 위에 있는 말들과 동시에 이동,extend:리스트안의 원소들 추가
                if len(graph_2[(nx, ny)]) >= 4:
                    return turn

                for h in up:  # 말의 정보 갱신
                    horse[h][0], horse[h][1] = nx, ny

                if state == 1:  # 말의 방향이 바뀐 경우 고려
                    horse[i][2] = nd

            # 이동하려는 칸이 빨간색인 경우
            elif graph[nx][ny] == Red:
                down = graph_2[(x, y)][:graph_2[(x, y)].index(i)]  # 해당말의 아래에 있는 말들
                up = graph_2[(x, y)][graph_2[(x, y)].index(i):]  # 해당말을 포함한 위에 있는 말들
                graph_2[(x, y)] = down

                up.reverse()
                graph_2[(nx, ny)].extend(up)  # 위에 있는 말들과 동시에 이동,extend:리스트안의 원소들 추가
                if len(graph_2[(nx, ny)]) >= 4:
                    return turn

                for h in up:  # 말의 정보 갱신
                    horse[h][0], horse[h][1] = nx, ny

                if state == 1:  # 말의 방향이 바뀐 경우 고려
                    horse[i][2] = nd

    return -1


if __name__ == "__main__":

    n, k = map(int, input().split())  # 체스판 크기nxn, 말의 갯수
    graph = [list(map(int, input().split())) for _ in range(n)]  # 체스판 색상 정보

    horse = dict()
    graph_2 = {(i, j): [] for j in range(n) for i in range(n)}

    for i in range(1, k + 1):
        x, y, d = map(int, input().split())
        horse[i] = [x - 1, y - 1, d - 1]
        graph_2[(x - 1, y - 1)].append(i)

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    White, Red, Blue = 0, 1, 2  # 체스판 색상에 따른 값

    revDir = {0: 1, 1: 0, 2: 3, 3: 2}

    result = moveHorse()

    print(result)