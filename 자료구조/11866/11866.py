n, m = map(int, input().split())
origin = [i for i in range(1, n + 1)]
answer = []
idx = 0
for _ in range(n):
  idx += m - 1
  idx %= len(origin)

  answer.append(origin.pop(idx))

print(f"<{', '.join(map(str,answer))}>")