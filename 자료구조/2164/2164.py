from collections import deque

if __name__ == "__main__":
  n = int(input())
  queue = deque()
  for i in range(1, n + 1):
    queue.append(i)

  while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

  print(queue.popleft())