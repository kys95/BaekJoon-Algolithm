import heapq
import sys
input = sys.stdin.readline

# 강의갯수 n 입력
n = int(input().rstrip())
# 강연 정보 담을 리스트
lectures = []
# 강연비, 강연디데이 입력
for _ in range(n):
    pay, dday = map(int, input().split())
    # 디데이, 강연비
    lectures.append((dday, pay))

def solution():
    # 디데이 기준으로 오름차순 정렬
    lectures.sort(key=lambda x: x[0])
    # 우선순위 큐
    heap = []
    # 디데이가 넘어가면 우선순위 큐에서 팝
    for lecture in lectures:
        heapq.heappush(heap, lecture[1])  # 강연비 푸쉬
        if len(heap) > lecture[0]:  # 디데이 넘어가면 팝
            heapq.heappop(heap)

    print(sum(heap))

if __name__ == "__main__":
    solution()