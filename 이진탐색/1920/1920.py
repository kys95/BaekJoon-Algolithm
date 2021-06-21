import sys
input = sys.stdin.readline
n = int(input())
# a오름차순 정렬
a = list(map(int, input().split()))
a = sorted(a)
m = int(input())
b = list(map(int, input().split()))
# 이진 탐색 함수
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) //2
        # target 확인
        if array[mid] == target:
            return 1
        # target이 기준보다 왼쪽에 있을 때
        elif array[mid] > target:
            end = mid - 1
        # target이 기준보다 오른쪽에 있을 때
        else:
            start = mid + 1
    return 0
for target in b:
    print(binary_search(a, target, 0, n - 1))
