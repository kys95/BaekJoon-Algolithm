import heapq
import sys
input = sys.stdin.readline

def solution(m):
    # 힙
    heap = []
    # 힙에 (10으로 나눈 나머지, 길이) 푸시
    for cake in cakes:
        heapq.heappush(heap, (cake % 10, cake))
    # 케이크 갯수
    count = 0

    while heap:
        x, y = heapq.heappop(heap)
        while y >= 10 and m >= 0:
            if y == 10:
                y -= 10
                count += 1

            elif y > 10:
                if m == 0:
                    break
                y -= 10
                m -= 1
                count += 1
    print(count)

if __name__ == '__main__':
    # 케이크 갯수n, 자를 수 있는 최대횟수 m 입력
    n, m = map(int, input().split())
    # 롤케이크 길이 입력
    cakes = list(map(int, input().split()))
    solution(m)