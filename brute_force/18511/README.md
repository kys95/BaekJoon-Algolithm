# 문제

1. N보다 작거나 같은 자연수 중, K의 원소로만 구성된 가장 큰 수를 출력해라.

2. 단, K의 모든 원소는 1~9까지의 자연수로만 구성된다.

   ex) N=657, K={1,5,7} -> 577



# 해결과정

1. N은 최대 9자릿수, K의 원소의 갯수는 최대 3이므로 중복순열을 구하여 완전탐색을 이용할 수 있다.
2. 중복순열을 구할때 N의 자릿수만큼  구하고, 만약 그 경우의 수들이 모두 N보다 클 때, N의 자릿수 - 1로 갱신하여 반복한다.