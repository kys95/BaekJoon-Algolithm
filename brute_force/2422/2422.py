import sys
input = sys.stdin.readline

# 아이스크림 종류갯수 n, 섞으면 안되는 조합 갯수 m 입력
n, m = map(int, input().split())
# 섞으면 안되는 조합 저장할 2차원 리스트
arr = [[] for _ in range(n + 1)]
# 섞으면 안되는 조합 정보 입력
for _ in range(m):
  a, b = map(int, input().split())
  arr[a].append(b)
  arr[b].append(a)

def solution():
  # 최종출력 갯수
  count = 0
  # n개 중 2개 뽑기
  for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
      if j in arr[i]:     # 섞으면 안되는 조합
        continue
      else:
        # 나머지 한개 뽑기
        for k in range(j + 1, n + 1):
          if k in arr[i]: # 섞으면 안되는 조합
            continue
          elif k in arr[j]: # 섞으면 안되는 조합
            continue
          else:
            count += 1
  print(count)

if __name__ == "__main__":
  solution()