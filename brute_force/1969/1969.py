import sys
input = sys.stdin.readline

# n, m 입력
n, m = map(int, input().split())
# DNA입력받을 리스트
DNAs = []
# n개의 DNA입력
for _ in range(n):
    DNAs.append(list(map(str, input().rstrip())))

def solution():
    result = ''  # 최종 출력 문자열
    count = 0  # 최종 출력 거리

    for i in range(m):
        a, c, g, t = 0, 0, 0, 0
        for j in range(n):
            if DNAs[j][i] == 'A':
                a += 1
            elif DNAs[j][i] == 'C':
                c += 1
            elif DNAs[j][i] == 'G':
                g += 1
            elif DNAs[j][i] == 'T':
                t += 1
        temp = max(a, c, g, t)
        if temp == a:
            result += 'A'
            count += c + g + t

        elif temp == c:
            result += 'C'
            count += a + g + t

        elif temp == g:
            result += 'G'
            count += a + c + t
        elif temp == t:
            result += 'T'
            count += a + c + g
    print(result)
    print(count)

if __name__ == "__main__":
    solution()