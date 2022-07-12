import sys
input = sys.stdin.readline
from math import inf

def dfs(idx, sub_total, nums, oper):
    global answer

    if idx == len(oper):  # 괄호안에 연산자를 삽입할 수 없음
        answer = max(answer, int(sub_total))
        return

    # (ㅁ + ㅁ) * ㅁ + ㅁ
    first = str(eval(sub_total + oper[idx] + nums[idx + 1]))
    dfs(idx + 1, first, nums, oper)

    # ㅁ + (ㅁ + ㅁ) * ㅁ + ㅁ
    if idx + 1 < len(oper):
        second = str(eval(nums[idx + 1] + oper[idx + 1] + nums[idx + 2]))
        second = str(eval(sub_total + oper[idx] + second))
        dfs(idx + 2, second, nums, oper)


if __name__ == "__main__":
    n = int(input())  # 수식의 길이
    data = list(map(str, input().rstrip()))  # 수식

    # 숫자와 연산자 분리
    nums = []
    oper = []
    for x in data:
        nums.append(x) if x.isdigit() else oper.append(x)

    answer = -inf

    dfs(0, nums[0], nums, oper)

    print(answer)