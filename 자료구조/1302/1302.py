if __name__ == "__main__":
  n = int(input())
  dic = {}
  for _ in range(n):
    book = input()
    if book in dic:
      dic[book] += 1
    else:
      dic[book] = 1

  max_value = max(dic.values())
  arr = []
  for k, v in dic.items():
    if v == max_value:
      arr.append(k)

  arr.sort()
  print(arr[0])