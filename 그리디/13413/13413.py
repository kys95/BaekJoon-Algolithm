import sys
input = sys.stdin.readline

def solution(n):
    # 초기문자열 기준 B, W 카운트 변수
    B_count, W_count = 0, 0
    # 초기문자열과 목표문자열 비교
    for i in range(n):
        if initial[i] != target[i]:
            if initial[i] == 'B':
                B_count += 1
            else:
                W_count += 1
    print(max(B_count, W_count))

if __name__ == '__main__':
    # 테스트 케이스 k입력
    k = int(input().rstrip())
    for _ in range(k):
        # 오셀로 말의 갯수 n입력
        n = int(input().rstrip())
        # 초기문자열, 목표문자열 입력
        initial = input().rstrip()
        target = input().rstrip()

        solution(n)