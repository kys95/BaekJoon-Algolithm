import sys
input = sys.stdin.readline

# 상담갯수 n입력
n = int(input().rstrip())
# n + 1일 퇴사
t = [0] * (n + 1)
p = [0] * (n + 1)
result = 0

for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

def solution(day, sum):
    global result

    # 상담중단
    if day == n + 1:
        result = max(result, sum)
        return

        # 상담이 기간을 넘어가는 경우
    if day > n + 1:
        return

    # 상담한다
    solution(day + t[day], sum + p[day])

    # 상담 안한다
    solution(day + 1, sum)

if __name__ == "__main__":
    solution(1, 0)
    print(result)