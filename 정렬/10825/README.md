# 문제

1. n명의 이름과 국어, 영어, 수학 점수가 주어질 때 다음과 같은 조건으로 정렬한다.
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로



# 해결과정

1. 튜플을 원소로 하여 순서에 맞게 정렬한다.

2. n이 100,000 까지 이므로 정렬 라이브러리를 이용한다.

3. key속성에 값을 대입하여 주어진 조건에 의해 정렬한다.

   