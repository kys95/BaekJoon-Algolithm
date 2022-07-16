def check(x, y):
    for i in range(1, x + 1):
        if board[x - i] == y or board[x - i] == y - i or board[x - i] == y + i:
            return False
    return True


def dfs(i):
    global cnt
    if i == n:
        cnt += 1
        return

    for j in range(n):
        if check(i, j):
            board[i] = j
            dfs(i + 1)
            board[i] = -1


if __name__ == "__main__":
    n = int(input())
    board = [-1] * n
    cnt = 0
    dfs(0)

    print(cnt)