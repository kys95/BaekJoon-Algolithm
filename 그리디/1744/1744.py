#n 입력받기
n=int(input())

#양수 리스트 초기화하기
pn=[]
#음수 리스트 초기화하기
nn=[]
#나머지 수 리스트 초기화하기
en=[]
#리스트에 숫자 집어넣기
for i in range(n):
  number=int(input())
  #number가 1보다 크면 양수리스트에 추가하기
  if number>1:
    pn.append(number)
  #0보다 작으면 음수리스트에 추가하기
  elif number<0:
    nn.append(number)
  else:
    en.append(number)

#양수리스트 큰순으로 정렬하기
pn.sort(reverse=True)
#음수리스트 작은순으로 정렬하기
nn.sort()

#정답 변수 초기화하기
result=0
#pn 길이가 짝수이면 그냥하고 홀수이면 남은 한개는 더해주기
if len(pn)%2==0:
  for i in range(0,len(pn)-1,2):
    result+=pn[i]*pn[i+1]
if len(pn)%2!=0:
  for i in range(0,len(pn)-1,2):
    result+=pn[i]*pn[i+1]
  result+=pn[-1]

#nn 길이가 짝수이면 그냥하고 홀수이면 남은 한개는 더해주기
if len(nn)%2==0:
  for i in range(0,len(nn)-1,2):
    result+=nn[i]*nn[i+1]
if len(nn)%2!=0:
  for i in range(0,len(nn)-1,2):
    result+=nn[i]*nn[i+1]
  #나머지 수에 0이 없다면 그냥 더해주기
  if 0 not in en:
    result+=nn[-1]
#en에 있는 1들 다 더해주기
result+=sum(en)
print(result)