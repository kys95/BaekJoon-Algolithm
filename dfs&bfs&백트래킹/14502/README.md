# 문제
1. 연구소의 빈칸에 벽 3개를 설치한다.
2. 바이러스는 상하좌우로 인접한 빈칸으로 퍼져나간다.
3. 바이러스가 퍼질수 없는 곳의 최댓값을 구한다.

# 해결과정
1. 조합 라이브러리를 이용한다. 전체 그래프 크기가 최대 8x8이므로  
   최악의 경우 <sub>64</sub>C<sub>3</sub> 즉, 100,000보다 작으므로 제한 시간 내에 해결할 수 있다.
   
2. dfs를 이용한다.
3. 완전탐색을 통해 안전 영역의 크기를 구한다.
