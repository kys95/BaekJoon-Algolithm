import heapq

n = int(input())
# 힙에 카드 묶음 삽입
heap = []
for i in range(n):
    card = int(input())
    heapq.heappush(heap, card)
# 카드 합
result = 0
# 힙에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개 카드 묶음 꺼냄
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    #카드 묶음을 합쳐서 다시 삽입
    sum = one + two
    result += sum
    heapq.heappush(heap, sum)
# 최소 합 출력
print(result)