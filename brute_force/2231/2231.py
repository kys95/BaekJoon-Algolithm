import sys
input = sys.stdin.readline

# 자연수 n 입력
n = int(input().rstrip())

def solution(n):
    for i in range(1, n + 1):
        # 분해합 하기 위해 리스트로 만듦
        num_list = list(map(int, str(i)))
        result = i + sum(num_list)  # 분해합

        if result == n:
            print(i)
            break
        if i == n:
            print(0)

if __name__ == "__main__":
    solution(n)