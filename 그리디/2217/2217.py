import sys
input = sys.stdin.readline

# 로프갯수 n 입력
n = int(input().rstrip())
# n개의 로프를 담을 리스트
ropes = []
# n개 로프 입력
for _ in range(n):
  ropes.append(int(input().rstrip()))

# 내림차순 정렬
ropes = sorted(ropes, reverse=True)
# 병렬 연결할 수 있는 무게 찾기
for i in range(n):
  ropes[i] = ropes[i] * (i + 1)

print(max(ropes))