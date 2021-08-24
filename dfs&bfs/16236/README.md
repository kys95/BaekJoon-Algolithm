# 문제

1. nxn크기의 공간에 물고기 m마리와 상어 1마리가 있다.
2. 아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.
3. 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
4. 아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.
   - 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
   - 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
   - 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
     - 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
     - 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
5. 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
6. 몇초 동안 물고기를 잡아먹을 수 있는지 구해라.



# 해결과정

1. 아기상어의 좌표를 저장하고 0으로 초기화한다.
2. 아기 상어의 좌표, 무게, 이동시간, 먹은 횟수를 bfs에 입력할 변수로 사용하고 초기화한다.
3. 다음 칸이 0이거나 무게가 같은 칸이면 q에 저장하고 이동한다.
4. 0과 아기상어의 무게 사이라면 canEat에 푸쉬한다.
5. canEat에 좌표가 있다면 pop하여 다음 좌표로 초기화한다.(heap이므로 가장 최선의 좌표)
6. bfs를 모두 돌고난 후 최종 time을 출력한다.