# 문제
1. 4x4 모든 좌표에 1~16번의 물고기가 있다.
2. 각 물고기는 8개중 하나의 방향을 가지고 있다.
3. 처음에 상어는 (0,0)에 물고기를 잡아먹고 시작한다. 상어는 잡아먹은 물고기의 방향을 가진다.
4. 그리고 모든 물고기들은 번호순으로 각 방향대로 움직인다.
5. 만약 방향으로 이동할 수 없는 경우, 즉 범위를 벗어나거나 해당 위치에 상어가 있다면 반시계방향으로 45도 이동한다.
   그렇게 8번이동해도 이동할 수 없다면 해당 물고기는 이동하지 않고 다음 물고기가 이동한다.
6. 모든 물고기가 이동하고 다시 상어가 해당방향에 위치한 모든 좌표로 움직일 수 있다. 어딜 먼저 이동할지는 미지수이다.
7. 이 과정을 반복하여 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구해라.



# 해결과정
1. 이 문제는 순서대로 상어가 물고기를 잡아먹고 물고기가 순번대로 이동하고 상어가 이동할 수 있는 리스트를 구해 그중 한곳으로 이동하는 것을
   반복하는 문제이다.
2. 처음에 입력받은 물고기 정보를 물고기리스트 fishes에 [물고기 번호, 물고기 방향]으로 데이터를 넣어준다.
3. 그리고 dfs를 통해 (0,0)부터 탐색한다.
4. 이때 상어가 이동하는 경우의 수가 여러개 이므로 똑같은 조건에 있어야 하므로 deepcopy 깊은 복사를 통해 fish를 이용한다.
5. 상어가 물고기를 처음에 잡아먹고 해당 위치에 상어가 있다는 표시로 -1로 갱신한다.
6. 그리고 물고기가 이동하는 moveFish함수를 호출한다.
7. moveFish함수는 물고기 번호 순서대로 탐색하는데 해당 물고기의 위치를 반환하는 함수 findFish를 통해 x,y값을 구하고 만약 없다면 
  상어한테 먹힌 물고기이므로 다음 순번의 물고기로 넘어간다. 물고기의 x,y,방향을 통해 nx,ny를 구하고 해당 위치가 상어가 위치하지 않고
  범위를 벗어나지 않는다면 물고기 위치를 교환한다. 만일 범위를 벗어나거나 상어의 위치라면 dir값을 갱신하여 8번 반복한다.
8. 그리고 상어가 이동할 수 있는 모든 경우의 수를 찾는 moveShark를 호출한다.
9. moveShark함수는 nx갑을 최대 3번 갱신할 수 있으므로 cases에 담아 반환한다. 
10. 반환받은 cases를 다시 dfs를 통해 탐색한다.