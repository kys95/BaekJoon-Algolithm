from itertools import combinations
import sys
input = sys.stdin.readline

# 출력할 L개의 소문자, 문자종류 C
L, C = map(int, input().split())
# 암호입력
data = list(input().split())
# 모음 배열
vowels = set(['a', 'e', 'i', 'o', 'u'])
# 오름차순 정렬
data = sorted(data)

codes = combinations(data, L)
for code in codes:
  # 최소 1개 모음 & 최소 2개 자음
  if 1 <= len(set(code) & vowels) <= L - 2:
    print(''.join(code))