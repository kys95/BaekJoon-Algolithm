# 문제

1. nxm 지도에서 각 칸에 높이가 있다.
2. 지도에서 지나갈 수 있는 길이란 한 행 또는 한 열 전부를 나타낸다.
3. 조건 

- 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
- 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
- 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.



# 해결과정

1. n행, m열 리스트를 받아서 지나갈 수 있는 길인지 검사해주는 check함수를 구현한다.
2. 앞 뒤 차이가 2이상 난다면 패스, 차이가 1난다면 경사로를 놓아준다. 단, 경사로가 놓아져 있거나 놓을 수 없다면 False를 리턴한다.