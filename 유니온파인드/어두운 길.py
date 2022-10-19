def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

if __name__ == "__main__":
  g = int(input())
  p = int(input())
  parent = [0] * (g + 1)
  for i in range(1, g + 1):
    parent[i] = i

  result = 0
  data = []
  for _ in range(p):
    data.append(int(input()))
  for i in range(len(data)):
    x = find_parent(parent, data[i])
    if x == 0:
      break
    union_parent(parent, x, x - 1)
    result += 1
  print(result)