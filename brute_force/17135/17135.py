import sys

input = sys.stdin.readline
from itertools import combinations
import heapq


def move_enemy():
    for i in range(-1, -n, -1):
        arr[i] = arr[i - 1]

    arr[0] = [0 for _ in range(m)]


def attack_enemy(case):
    cnt = 0

    remove_enemy_list = []
    attacked = [[False for _ in range(m)] for _ in range(n)]  # 공격받은지 확인리스트

    for archor in case:  # 각 궁수의 위치
        heap = []

        for i in range(n - 1, -1, -1):
            for j in range(m):
                if arr[i][j] == 1:
                    dist = abs(n - i) + abs(archor - j)
                    if dist <= d:
                        heapq.heappush(heap, [dist, j, i])  # 죽이는 우선순위 1.거리 2.y좌표 3.x좌표

        if heap:
            dist, y, x = heapq.heappop(heap)
            remove_enemy_list.append([x, y])

    for x, y in remove_enemy_list:
        if not attacked[x][y]:
            attacked[x][y] = True
            cnt += 1
            arr[x][y] = 0  # 적 제거

    return cnt


def get_enemy_count():
    cnt = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1

    return cnt


def simulation(case):
    cnt = 0

    while get_enemy_count() != 0:  # 적이 좌표에서 사라질때 까지
        cnt += attack_enemy(case)  # 적 공격
        move_enemy()  # 적 이동

    return cnt


if __name__ == "__main__":
    n, m, d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    cases = list(combinations([x for x in range(m)], 3))  # 궁수 3명을 배치하는 모든 경우의 수

    arr = []  # 궁수 3명을 배치하는 각 경우의 수에 대한 graph
    answer = 0  # 제거할 수 있는 최대의 적 수

    for case in cases:
        arr = [[graph[x][y] for y in range(m)] for x in range(n)]  # 각 경우마다 graph가 같아야하므로
        cnt = simulation(case)  # 하나의 경우에서 발생하는 적의 제거 수

        if answer < cnt:
            answer = cnt

    print(answer)