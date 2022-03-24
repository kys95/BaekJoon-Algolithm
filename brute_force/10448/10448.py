import sys
input = sys.stdin.readline

triangle = [n * (n + 1) // 2 for n in range(1, 46)]
eureka = [0] * 1001

for a in triangle:
  for b in triangle:
    for c in triangle:
      if a + b + c <= 1000:
        eureka[a + b + c] = 1

t = int(input())
data = []
for _ in range(t):
  data.append(int(input()))
for x in data:
  print(eureka[x])