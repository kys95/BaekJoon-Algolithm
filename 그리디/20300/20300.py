import sys
input = sys.stdin.readline

# 운동기구 갯수 n 입력
n = int(input().rstrip())
# 근손실 입력
muscle = list(map(int, input().split()))
# 오름차순 정렬
muscle.sort()
# 최소 근손실 합
M = 0
if n % 2 == 0:
  for i in range(n // 2):
    M = max(M, muscle[i] + muscle[n - 1 - i])
else:
  for i in range(n // 2):
    M = max(M, muscle[i] + muscle[n - 2 - i])
  M = max(M, muscle[-1])
print(M)