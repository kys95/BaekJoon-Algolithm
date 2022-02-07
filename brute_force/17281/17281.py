import sys
input = sys.stdin.readline
from itertools import permutations

def find_score(order, board, n):
    score = 0
    idx = 0
    for inning in range(n):
        out = 0
        base1, base2, base3 = 0, 0, 0

        while out != 3:
            if board[inning][order[idx % 9]] == 0:  # 아웃
                out += 1
            elif board[inning][order[idx % 9]] == 1:  # 1루타
                score += base3
                base3, base2, base1 = base2, base1, 1
            elif board[inning][order[idx % 9]] == 2:  # 2루타
                score += (base3 + base2)
                base3, base2, base1 = base1, 1, 0
            elif board[inning][order[idx % 9]] == 3:  # 3루타
                score += (base3 + base2 + base1)
                base3, base2, base1 = 1, 0, 0
            else:  # 홈런
                score += (base3 + base2 + base1 + 1)
                base3, base2, base1 = 0, 0, 0

            idx += 1

    return score

if __name__ == "__main__":
    n = int(input())

    # 각 선수가 n개의 이닝에서 얻는 결과
    board = []
    for _ in range(n):
        data = list(map(int, input().split()))
        board.append(data)

    orders = list(permutations([x for x in range(1, 9)], 8))  # 4번타자를 제외한 8명의 선수타순의 모든 조합

    answer = 0
    for order in orders:
        order = list(order[:3]) + [0] + list(order[3:])
        answer = max(answer, find_score(order, board, n))

    print(answer)
