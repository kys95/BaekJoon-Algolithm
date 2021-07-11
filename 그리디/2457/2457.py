import sys
input = sys.stdin.readline

# 꽃들의 갯수
n = int(input().rstrip())
# 꽃에 관한 정보 담을 리스트
flowers = []
# 꽃이 피는 시기, 지는 시기 입력
for _ in range(n):
  start_m, start_d, end_m, end_d = map(int, input().split())
  start = start_m * 100 + start_d
  end = end_m * 100 + end_d
  flowers.append((start, end))

def solution(n):
  # 1.꽃이 피는 시기 2.꽃이 지는 시기 기준으로 오름차순 정렬
  flowers.sort(key=lambda x:(x[0], x[1]))
  date = 301  # 기준날짜
  temp = 0    # date기준에 속하면서 꽃이 지는 시기가 가장 긴 것
  index = -1
  result = 0  # 최종 꽃의 종류 갯수
  while date <= 1130 and index < n:
    index += 1
    flag = False
    for i in range(index, n):
      if flowers[i][0] > date:  break # 꽃이 매일 피지 못하는 경우
      if flowers[i][1] > temp:        # 꽃이 지는 시기 가장 긴것 찾기
        temp = flowers[i][1]
        index = i
        flag = True
    if flag:
      result += 1
      date = temp
    else:
      return print(0)

  return print(result)

if __name__ == '__main__':
  solution(n)
