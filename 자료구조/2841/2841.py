if __name__ == "__main__":
    n, p = map(int, input().split())
    stack = [[] for _ in range(7)]
    answer = 0
    for _ in range(n):
        line, fret = map(int, input().split())
        while stack[line] and stack[line][-1] > fret:
            stack[line].pop()
            answer += 1
        if stack[line] and stack[line][-1] == fret:
            continue
        stack[line].append(fret)
        answer += 1

    print(answer)


# 1. 독립적인 기타줄에 프렛들의 번호가 오름차순이어야 한다.
# 2. 가장 최근에 누른 프렛의 번호보다 현재 프렛 번호가 작다면 현재 프렛 번호가 크거나 같을 때까지 빼낸다 -> 스택으로 구현
# 3. 기타줄의 번호는 독립적이므로 1부터 6개의 기타줄을 초기화하고 각 기타줄에 프렛번호를 비교하면 된다.