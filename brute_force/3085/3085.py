import sys
input = sys.stdin.readline

def check(board):
    answer = 1
    for i in range(n):
        cnt = 1
        for j in range(n):
            if j + 1 < n:
                if board[i][j] == board[i][j + 1]:
                    cnt += 1
                else:
                    cnt = 1
                if cnt > answer:
                    answer = cnt

    for j in range(n):
        cnt = 1
        for i in range(n):
            if i + 1 < n:
                if board[i][j] == board[i + 1][j]:
                    cnt += 1
                else:
                    cnt = 1
                if cnt > answer:
                    answer = cnt

    return answer


def change(board):
    result = 1
    for i in range(n):
        for j in range(n):
            if j + 1 < n:
                if board[i][j] != board[i][j + 1]:  # 색다르면 교환
                    board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                    temp = check(board)  # 가장 긴부분 찾기
                    if temp > result:
                        result = temp

                    board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

            if i + 1 < n:
                if board[i][j] != board[i + 1][j]:
                    board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                    temp = check(board)
                    if temp > result:
                        result = temp

                    board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

    return result


if __name__ == "__main__":
    n = int(input())  # 격자크기
    board = [list(map(str, input().rstrip())) for _ in range(n)]  # 보드에 사탕놓음

    print(change(board))  # 색이 다른 인접한 두개의 칸 교환
