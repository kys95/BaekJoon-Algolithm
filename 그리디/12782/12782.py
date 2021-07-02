import sys
input = sys.stdin.readline

t = int(input())  #테스트 케이스 개수

for _ in range(t):
    n, m = map(str, input().split())  # 이진수1, 이진수2
    one = 0
    zero = 0
    for i in range(len(m)):
        if n[i] != m[i]:
            if m[i] == '1':
                one += 1
            else:
                zero += 1
    print(max(one, zero))