import sys
input = sys.stdin.readline

# 마을 갯수 n 입력
n = int(input().rstrip())
# 마을정보 담을 리스트
towns = []
# 전체 인구수
people = 0
# 마을위치, 인구수 입력
for i in range(n):
  pos, num = map(int, input().split())
  towns.append((pos, num))
  people += num


def solution(people):
  # 마을 위치를 기준으로 오름차순 정렬
  towns.sort(key =lambda x:x[0])
  # 전체인구의 절반
  mid = people // 2
  # 전체인구수가 홀수일 때
  if people % 2 == 1:
    mid += 1
  # 인구 카운트 변수
  count = 0
  for pos, num in towns:
    count += num
    if count >= mid:
      print(pos)
      break

if __name__ == '__main__':
  solution(people)
