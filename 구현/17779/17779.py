import sys

input = sys.stdin.readline
INF = int(1e9)
# 재현시의 크기 n
n = int(input().rstrip())
graph = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
# 인구총합
total = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        total += graph[i][j]

def solution(x, y, d1, d2):
    # 2번조건
    temp = [[0] * (n + 1) for _ in range(n + 1)]
    temp[x][y] = 5
    for i in range(1, d1 + 1):
        temp[x + i][y - i] = 5
    for i in range(1, d2 + 1):
        temp[x + i][y + i] = 5
    for i in range(d2 + 1):
        temp[x + d1 + i][y - d1 + i] = 5
    for i in range(d1 + 1):
        temp[x + d2 + i][y + d2 - i] = 5

    people = [0] * 5  # 각 선거구의 인구수
    # 1번 선거구
    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if temp[r][c] == 5:
                break
            people[0] += graph[r][c]

    # 2번 선거구
    for r in range(1, x + d2 + 1):
        for c in range(n, y, -1):
            if temp[r][c] == 5:
                break
            people[1] += graph[r][c]

    # 3번 선거구
    for r in range(x + d1, n + 1):
        for c in range(1, y - d1 + d2):
            if temp[r][c] == 5:
                break
            people[2] += graph[r][c]

    # 4번 선거구
    for r in range(x + d2 + 1, n + 1):
        for c in range(n, y - d1 + d2 - 1, -1):
            if temp[r][c] == 5:
                break
            people[3] += graph[r][c]

    # 5번 선거구
    people[4] += total - sum(people)
    return max(people) - min(people)

if __name__ == "__main__":
    result = INF
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            for d1 in range(1, n + 1):
                for d2 in range(1, n + 1):
                    if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                        result = min(result, solution(x, y, d1, d2))

    print(result)