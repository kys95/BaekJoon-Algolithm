# 문제

1. 만들고자 하는 단어를 n개의 전공책 문자열 조합으로 만들고자 한다.
2. 각각의 문자열들은 가격이 주어지고 최소한의 가격으로 만들고자 하는 단어를 만들어야한다.
3. 만들 수 없다면 -1을 출력해라.



# 해결과정

1. 전공책을 사용하는 모든 경우의 수는 최대  2<sup>16</sup> 이고,  만들고자 하는 단어의 길이가 10이하이므로 완전탐색을 이용한다.
2. 최소 1개의 전공책을 사용해야 하므로 1부터 n개의 전공책 조합을 만들고, 이를 하나의 문자열 name으로  갱신하고 가격을 갱신한다. 
3. 각 경우의 수를 주어진 단어의 문자와 일대일 비교하여 있다면 name에서 삭제하고 없다면 return한다. 비교가 모두 끝난 후에는 만들고자 하는 단어의 문자들이 모두 속해있다는 뜻이므로 가격을 최솟값으로 갱신한다.