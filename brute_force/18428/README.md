# 문제

1. 선생님은 자신의 위치에서 상,하,좌,우 방향으로 학생들을 감시한다.

   단, 장애물 뒤에 있는 학생은 볼 수 없다.

2. 빈칸에 장애물 3개를 설치한다. 

3. 학생이 선생님의 감시를 피할 수 있다면 "YES", 없다면 "NO"를 출력한다.



# 해결과정

1. 복도의 크기는 NxN(3<=N<=6), 장애물 3개를 설치하는 조합의 수는 

   최악의 경우 <sub>36</sub>C<sub>3</sub> 이 된다. 이는 10,000이하이므로 완전 탐색을 이용할 수 있다.

2. 선생님의 위치를 각각 확인하고 상,하,좌,우를 확인하여 감지여부를 확인한다.