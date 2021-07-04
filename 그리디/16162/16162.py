import sys
input = sys.stdin.readline

# 음의갯수 n, 첫항 a, 공차 d 입력
n, a, d = map(int, input().split())
# 음 입력
notes = list(map(int, input().split()))

def solution(a, d):
    # ?단 고음 카운트
    count = 0
    for note in notes:
        if a == note:
            a += d
            count += 1
    print(count)

if __name__ == '__main__':
    solution(a, d)