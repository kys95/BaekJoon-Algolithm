import sys

input = sys.stdin.readline
from itertools import permutations
from copy import deepcopy

def rotate(copy_graph, case):
    x, y, s = case

    for i in range(s, 0, -1):
        tmp = copy_graph[x - i][y - i]  # 왼쪽 위 모서리 담아둠

        for r in range(x - i, x + i):  # 좌측 세로를 위로 옮김
            copy_graph[r][y - i] = copy_graph[r + 1][y - i]

        for c in range(y - i, y + i):  # 아래측 가로를 왼쪽으로 옮김
            copy_graph[x + i][c] = copy_graph[x + i][c + 1]

        for r in range(x + i, x - i, -1):  # 우측 세로를 아래로 옮김
            copy_graph[r][y + i] = copy_graph[r - 1][y + i]

        for c in range(y + i, y - i + 1, -1):  # 위측 가로를 오른쪽으로 옮김
            copy_graph[x - i][c] = copy_graph[x - i][c - 1]

        copy_graph[x - i][y - i + 1] = tmp


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    cases = [list(map(int, input().split())) for _ in range(k)]

    INF = int(1e9)
    cases = list(permutations(cases, k))  # 모든 경우의 수

    answer = INF
    for case in cases:
        copy_graph = deepcopy(graph)

        for data in case:
            x, y, s = data
            data = x - 1, y - 1, s
            rotate(copy_graph, data)

        for r in copy_graph:
            answer = min(answer, sum(r))

    print(answer)