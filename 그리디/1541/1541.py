import sys
input = sys.stdin.readline
# 처음에 -기준으로 나눔
arr = input().split('-')
# 최소합
s = 0
for i in arr[0].split('+'):
  s += int(i)
# 이후부터 +오면 -로 전환
for i in arr[1:]:
  for j in i.split('+'):
    s -= int(j)
print(s)
