# 문제

1. N + 1일째 퇴사, N일동안 상담을 진행한다.
2. 상담동안 백준이가 얻을 수 있는 최대 수익을 구해라.



# 해결과정

1. N이 최대 15이므로 N개의 상담을 하는지 or 안하는지에 관한 모든 경우의 수는 최대 32,768이다. 이에 따라 모든 경우의 수를 탐색한다.
2. 1일부터 상담하는지 or 안하는지 재귀로 탐색하여 각 경우의 수에 따른 비용 sum과 비교하여 최댓값을 result로 갱신한다.