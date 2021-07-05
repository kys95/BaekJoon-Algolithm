import sys
input = sys.stdin.readline

def solution(m):
    # 박스에 넣을 수 있는 무게
    weight = m
    # 박스 갯수
    count = 1
    for book in books[::-1]:
        # 박스에 책 넣을 수 있는 경우
        if weight >= book:
            weight -= book
        else:
            weight = m - book
            count += 1
    print(count)

if __name__ == '__main__':
    # 책의 갯수 n, 박스에 넣을 수 있는 최대 무게 m 입력
    n, m = map(int, input().split())
    # 책 무게 입력
    books = list(map(int, input().split()))
    if n == 0:
        print(0)
    else:
        solution(m)