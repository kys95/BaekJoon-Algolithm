import sys
input = sys.stdin.readline

# 시험장 갯수 n 입력
n = int(input().rstrip())
# 응시자 수 입력
people = list(map(int, input().split()))
# 총감독관, 부감독관 감시자 수 b, c입력
b, c = map(int, input().split())

def solution(people, b, c, n):
  count = n                # 시험장 마다 총감독관 들어감
  for person in people:
    if (person - b) > 0:   # 부감독관이 필요하다면
      if (person - b) % c == 0:
        count += (person - b) // c
      else:
        count += (person - b) // c + 1

  print(count)


if __name__ =="__main__":
  solution(people, b, c, n)