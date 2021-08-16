from collections import Counter
import sys
input = sys.stdin.readline

# r,c,k
r, c, k = map(int, input().split())
r -= 1;
c -= 1
# 배열 A
A = [list(map(int, input().split())) for _ in range(3)]
time = 0  # 시간


def solution(time, A):
    while time <= 100:
        if r < len(A) and c < len(A[0]) and A[r][c] == k:
            return time
        # c연산인지 확인
        cflag = False
        if len(A[0]) > len(A):
            A = list(zip(*A))
            cflag = True

        # 연산
        max_len = 0
        tmp_a = []

        for now_row in A:
            ct = Counter(now_row)
            if ct.get(0):
                del ct[0]
            num_cnt = list(map(list, ct.items()))
            num_cnt.sort(key=lambda x: (x[1], x[0]))
            tmp_a.append(list(sum(num_cnt, []))[:100])
            max_len = max(max_len, len(tmp_a[-1]))

        # 0채우기
        for i in range(len(tmp_a)):
            if len(tmp_a[i]) < max_len:
                tmp_a[i] += [0] * (max_len - len(tmp_a[i]))

        A = tmp_a
        # C연산인 경우 다시 복귀
        if cflag:
            A = list(zip(*A))
        time += 1

    return time

if __name__ == "__main__":
    result = solution(time, A)
    if result >= 101:
        print(-1)
    else:
        print(result)