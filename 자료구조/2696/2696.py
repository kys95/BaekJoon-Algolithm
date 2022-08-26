import heapq


def put(v):
    if max_heap and v > -max_heap[0]:
        heapq.heappush(min_heap, v)
    else:
        heapq.heappush(max_heap, -v)

    if len(max_heap) > len(min_heap) + 2:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        ipt = []
        for _ in range(n // 10 + 1 if n % 10 else n // 10):
            ipt += list(map(int, input().split()))

        max_heap = []
        min_heap = []
        ans = []
        for i, v in enumerate(ipt):
            put(v)
            if i % 2 == 0:
                ans.append(-max_heap[0])

        print(len(ans))
        for i in range(len(ans) // 10 + 1 if len(ans) % 10 else len(ans) // 10):
            print(*ans[i * 10:(i + 1) * 10])

# if __name__ == "__main__":
#     for _ in range(int(input())):
#         n = int(input())
#         ipt = []
#         for _ in range(n // 10 + 1 if n % 10 else n // 10):
#             ipt += list(map(int, input().split()))
#
#         temp = []
#         ans = []
#         for i, v in enumerate(ipt):
#             temp.append(v)
#             if i % 2 == 0:
#                 temp.sort()
#                 ans.append(temp[i // 2])
#
#         print(len(ans))
#         for i in range(len(ans) // 10 + 1 if len(ans) % 10 else len(ans) // 10):
#             print(*ans[i * 10: (i + 1) * 10])


# 1. 입력을 10개 단위로 끊어서 받고 출력도 10개 단위로 끊어서 출력해야 함. -> n개에 따라 개행
# 2. 리스트 temp과 ans를 두고 temp에는 입력받은 원소들을 삽입하고 홀수번째마다 정렬을 하여 중간값을 ans에 삽입한다.
# 3. 이 방법은 n만큼 돌면서 두 번에 한 번 꼴로 정렬을 하므로 시간복잡도는 O(M<sup>2</sup>logM)이다.
# 3. 우선순위 큐를 이용하면 시간복잡도를 줄일 수 있다.
# 4. 최대힙에는 중간값과 그 이하의 값들, 최소힙에는 중간값보다 항상 큰값을 넣어주면 최대힙의 루트에는 항상 중간값이 오게 된다.
# 5. 우선순위 큐에서 값을 한 번 넣거나 뺄 때에는 O(logM)이고 이는 반복문을 M만큼 돌면서 1~3번씩 수행된다.
#    -> 최대힙과 최소힙 크기의 균형을 맞추기 위해서 추가로 한쪽 우선순위 큐에 값을 빼서 다른 쪽 우선순위 큐에 넣어 준다.
