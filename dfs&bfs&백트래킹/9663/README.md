### 해결과정
1. board를 -1를 가지는 n개의 배열로 초기화한다.ex) board[0]=1 -> 0행 1열에 퀸이 있다. 
2. 전역변수 cnt를 0으로 초기화하고 1행부터 어느 열에 둘지 확인한다. ->같은 행, 같은 열, 같은 대각선에 둘 수 없음.
3. 만일, i행 j열에 둘 수 있다면 board[i] = j로 갱신하고 i + 1행을 탐색한다.
4. n행이 되면 cnt를 +1하고 return한다.
5. cnt를 출력한다.