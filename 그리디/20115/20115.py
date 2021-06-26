import sys
input = sys.stdin.readline

# 에너지 드링크 갯수 n 입력
n = int(input().rstrip())
# n개의 에너지 드링크 양 입력
drinks = list(map(int, input().split()))
# 양이 가장 많은 에너지드링크
big = max(drinks)
# 최대의 드링크 양 출력
print('%g'%((sum(drinks) - big) / 2 + big))