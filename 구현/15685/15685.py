import sys
input = sys.stdin.readline

# 드래곤커브 갯수 n
n = int(input().rstrip())
# 커브 방향
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
# 드래곤 커브 정보
curv = []
for _ in range(n):
    x, y, d, g = map(int, input().split())
    curv.append((x, y, d, g))
# 그래프 초기화
graph = [[0] * 101 for _ in range(101)]

def solution():
    for x, y, d, g in curv:
        dir = []
        dir.append(d)  # 0세대
        graph[x][y] = 1
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx <= 100 and 0 <= ny <= 100:
            graph[nx][ny] = 1
            x, y = nx, ny
            # 1세대~g세대
            for gen in range(1, g + 1):
                temp = list(reversed(dir))
                for d in temp:
                    d = (d + 1) % 4
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx <= 100 and 0 <= ny <= 100:
                        graph[nx][ny] = 1
                        x, y = nx, ny
                        dir.append(d)
    result = 0
    for i in range(100):
        for j in range(100):
            if graph[i][j]:
                if graph[i + 1][j] and graph[i + 1][j + 1] and graph[i][j + 1]:
                    result += 1

    print(result)

if __name__ == "__main__":
    solution()