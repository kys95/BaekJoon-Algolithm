import heapq
import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # n = int(input())
    # hq = []
    # for _ in range(n):
    #   x = int(input())
    #   if x == 0:
    #     print(heapq.heappop(hq)[1] if hq else 0)
    #   else:
    #     heapq.heappush(hq, (abs(x), x))
    n = int(input())
    min_heap = []
    max_heap = []
    for _ in range(n):
        x = int(input())
        if x > 0:
            heapq.heappush(min_heap, x)
        elif x < 0:
            heapq.heappush(max_heap, -x)
        else:
            if min_heap:
                if len(max_heap) == 0 or min_heap[0] < max_heap[0]:
                    print(heapq.heappop(min_heap))
                else:
                    print(-heapq.heappop(max_heap))
            else:
                print(-heapq.heappop(max_heap) if max_heap else 0)