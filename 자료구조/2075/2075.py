import heapq

if __name__ == "__main__":
  n = int(input())
  hq = []
  for i in range(n):
    data = list(map(int, input().split()))
    for num in data:
      if len(hq) >= n:
        heapq.heappushpop(hq, num)
      else:
        heapq.heappush(hq, num)

  print(heapq.heappop(hq))