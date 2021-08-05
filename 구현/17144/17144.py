import sys
input = sys.stdin.readline
# r,c,t입력
r, c, t = map(int, input().split())
# 동, 남, 서,북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 미세먼지
graph = [list(map(int, input().split())) for _ in range(r)]

# 공기청정기 위치확인
def findCleaner():
    for i in range(r):
        if graph[i][0] == -1:
            return i

# 미세먼지 이동
def dust():
    temp = [[0] * c for _ in range(r)]  # 확산값 저장

    for x in range(r):
        for y in range(c):
            if graph[x][y] >= 5:
                count = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < r and 0 <= ny < c:

                        if graph[nx][ny] != -1:
                            temp[nx][ny] += graph[x][y] // 5
                            count += graph[x][y] // 5
                temp[x][y] -= count

    for x in range(r):
        for y in range(c):
            graph[x][y] += temp[x][y]

def clean():
    # up
    # 아래
    for i in range(up[0] - 1, 0, -1):
        graph[i][0] = graph[i - 1][0]

    # 왼
    for i in range(0, c - 1):
        graph[0][i] = graph[0][i + 1]

    # 위
    for i in range(0, up[0]):
        graph[i][c - 1] = graph[i + 1][c - 1]

    # 오
    for i in range(c - 1, 1, -1):
        graph[up[0]][i] = graph[up[0]][i - 1]
    graph[up[0]][1] = 0

    # down
    # 위
    for i in range(down[0] + 1, r - 1):
        graph[i][0] = graph[i + 1][0]

    # 왼
    for i in range(0, c - 1):
        graph[r - 1][i] = graph[r - 1][i + 1]

    # 아래
    for i in range(r - 1, down[0], -1):
        graph[i][c - 1] = graph[i - 1][c - 1]

    # 오
    for i in range(c - 1, 1, -1):
        graph[down[0]][i] = graph[down[0]][i - 1]

    graph[down[0]][1] = 0

if __name__ == "__main__":

    idx = findCleaner()
    up = (idx, 0)
    down = (idx + 1, 0)

    for _ in range(t):
        dust()
        clean()
    result = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                result += graph[i][j]
    print(result)