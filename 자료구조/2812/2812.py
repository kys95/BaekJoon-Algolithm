import sys
input = sys.stdin.readline

# 숫자의 자릿수 n, 삭제할 갯수 k 입력
n, k = map(int, input().split())
# n자리 숫자 입력
number = list(map(int, input().rstrip()))

def solution():
    global k
    # 최대 숫자 넣을 스택
    result = []
    # 모든 숫자 비교
    for i in range(n):
        while k > 0 and result and result[-1] < number[i]:
            # 숫자 팝
            result.pop()
            # 삭제했으니 -1
            k -= 1
        # 상대적으로 큰 숫자 삽입
        result.append(number[i])
    # 삭제할 것이 남아있을 경우
    while k > 0:
        result.pop()
        k -= 1
    # 최종 출력
    for num in result:
        print(num, end='')

if __name__ == '__main__':
    solution()