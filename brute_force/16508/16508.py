from itertools import combinations
import sys

input = sys.stdin.readline
INF = int(1e9)

# 만들고자 하는 단어
target = input().rstrip()
# 전공책 갯수 n 입력
n = int(input().rstrip())
# 전공책 정보 담을 리스트
books = []
# n개의 전공책 가격, 제목 입력
for _ in range(n):
    pr, na = map(str, input().split())
    books.append((int(pr), na))
result = INF

def solution(price, name):
    global result
    for i in range(len(target)):
        # 만들고자 하는 단어와 조합 비교
        if target[i] in name:
            name.remove(target[i])
        else:
            return

    result = min(result, price)
    return

if __name__ == "__main__":
    # 1~n개 고르는 조합
    for i in range(1, n + 1):
        choices = combinations(books, i)
        for choice in choices:
            price = 0
            name = ''
            # 각각의 경우의 수에 대한 가격, 문자열 합침
            for pr, na in choice:
                price += pr
                name += na

            solution(price, list(name))

    if result != INF:
        print(result)
    else:
        print(-1)




