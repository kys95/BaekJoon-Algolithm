import sys
input = sys.stdin.readline

# 문자의 갯수 n 입력
n = int(input().rstrip())
# 문자입력
arr = list(input().rstrip())

# 'B'& 'R' 카운트 변수
count_B = 0
count_R = 0

# 첫 번째 문자 확인
if arr[0] == 'B':
  count_B += 1
else:
  count_R += 1
# 두 번째 이후부터 문자 확인
for i in range(1, n):
  # 이전의 문자와 다르다면
  if arr[i] != arr[i - 1]:
    # 문자 B일때 B 카운트 + 1
    if arr[i] == 'B':
      count_B += 1
    else:
      count_R += 1
# 카운트가 큰 문자를 통으로 1로 취급
print(min(count_B, count_R) + 1)