from itertools import combinations
import sys

input = sys.stdin.readline
INF = int(1e9)

# 사람 수 n 입력
n = int(input().rstrip())
# 그래프 초기화
graph = [[0] * (n + 1) for _ in range(n + 1)]
# 능력치 정보 입력
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    for j in range(1, len(data) + 1):
        graph[i][j] = data[j - 1]
result = INF


def solution(n):
    global result
    # 스타트팀 조합&링크팀 조합
    Startchoices = list(combinations(list(range(1, n + 1)), n // 2))
    Linkchoices = Startchoices[::-1]

    for i in range(len(Startchoices) // 2):
        StartTeam, LinkTeam = 0, 0
        for x in Startchoices[i]:
            for y in Startchoices[i]:
                StartTeam += graph[x][y]

        for x in Linkchoices[i]:
            for y in Linkchoices[i]:
                LinkTeam += graph[x][y]

        result = min(result, abs(StartTeam - LinkTeam))


if __name__ == "__main__":
    solution(n)
    print(result)