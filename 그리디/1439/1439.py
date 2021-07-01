import sys
input = sys.stdin.readline

# 문자열 s 입력
s = input().rstrip()
# 0, 1 카운트 변수
count_of_0 = 0
count_of_1 = 0
# 첫문자 판별
if s[0] == '0':
  count_of_0 += 1
else:
  count_of_1 += 1

for i in range(1, len(s)):
  # 전의 문자와 다르면
  if s[i] != s[i - 1]:
    # 현재 문자가 0이라면
    if s[i] == '0':
      count_of_0 += 1
    else:
      count_of_1 += 1

print(min(count_of_0, count_of_1))