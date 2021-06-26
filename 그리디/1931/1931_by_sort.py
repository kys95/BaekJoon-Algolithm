import sys
input = sys.stdin.readline
n = int(input().rstrip())
result = []
time = []
for _ in range(n):
  start, end = map(int, input().split())
  result.append((start, end))
# 회의 끝나는 시간, 시작하는 시간 기준으로 오름차순 정렬
result.sort(key=lambda x: (x[1], x[0]))
time.append(result[0])
std = 0

for i in range(1, n):
  if result[std][1] <= result[i][0]:
    time.append(result[i])
    std = i

print(len(time))