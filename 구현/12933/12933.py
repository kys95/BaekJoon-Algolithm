import sys

input = sys.stdin.readline


def solve(start):
    global cnt

    first = True
    std = 'quack'
    j = 0

    for i in range(start, len(duck)):
        if not visited[i] and duck[i] == std[j]:
            visited[i] = True
            if duck[i] == 'k':
                if first:
                    first = False
                    cnt += 1
                j = 0
                continue

            j += 1


if __name__ == "__main__":
    duck = input().rstrip()

    if len(duck) % 5 != 0 or duck[0] != 'q':  # 오리개수가 0인 경우
        print(-1)
        sys.exit()

    visited = [False] * len(duck)  # 방문리스트
    cnt = 0

    for i in range(len(duck)):
        if not visited[i] and duck[i] == 'q':
            solve(i)

    if not all(visited) or cnt == 0:
        print(-1)
    else:
        print(cnt)