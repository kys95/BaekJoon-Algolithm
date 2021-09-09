from collections import deque
import sys

sys.setrecursionlimit(99999)
input = sys.stdin.readline

# 원반갯수 n, 정수갯수 m, 회전횟수 t
n, m, t = map(int, input().split())
# 원반
graph = []
for _ in range(n):
    graph.append(deque(list(map(int, input().split()))))
# 원반번호 x, 방향 d, 칸이동 k
r = []
for _ in range(t):
    r.append(list(map(int, input().split())))

# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 회전
def rotate(graph, x, d, k):
    for i in range(n):
        if (i + 1) % x == 0:
            if d == 0:  # 시계 방향
                graph[i].rotate(k)
            else:
                graph[i].rotate(-k)

# 인접한 수 찾음
def find(graph, x, y, res):
    global flag

    for d in range(4):
        nx = x + dx[d];
        ny = y + dy[d]
        if 0 <= nx < n and -1 <= ny < m + 1:
            if ny == -1:
                ny = m - 1
            elif ny == m:
                ny = 0

            if res == graph[nx][ny]:
                flag = True
                graph[x][y] = 'x'
                graph[nx][ny] = 'x'
                find(graph, nx, ny, res)

if __name__ == "__main__":
    # 회전
    for i in range(t):
        x, d, k = r[i][0], r[i][1], r[i][2]
        rotate(graph, x, d, k)  # 회전

        flag = False
        for i in range(n):
            for j in range(m):
                if graph[i][j] != 'x':
                    res = graph[i][j]
                    find(graph, i, j, res)

        if flag == False:
            temp = 0
            cnt = 0
            for i in range(n):
                for j in range(m):
                    if graph[i][j] != 'x':
                        temp += graph[i][j]
                        cnt += 1
            if cnt != 0:
                temp = temp / cnt
                for i in range(n):
                    for j in range(m):
                        if graph[i][j] != 'x':
                            if temp < graph[i][j]:
                                graph[i][j] -= 1
                            elif temp > graph[i][j]:
                                graph[i][j] += 1

    ans = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 'x':
                ans += graph[i][j]
    print(ans)