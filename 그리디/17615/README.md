# 문제

1. 빨간색, 파란색 볼이 일직선에 랜덤하게 놓여있을 때 볼을 옮겨서 같은 색 볼끼리 인접하게 놓이게 해야한다.
2. 볼을 옮길때 바로 옆에 다른 색깔의 볼이 있으면 그 볼을 모두 뛰어 넘을 수 있고, 옮길 수 있는 볼의 색깔의 한 가지이다.
3. 볼을 이동하여 같은 색끼리 모으되 최소 이동횟수를 구해라.



# 해결과정

1. 볼을 이동하는 경우의 수는 빨간색을 오른쪽, 왼쪽으로 옮기는 경우 & 파란색을 오른쪽, 왼쪽으로 옮기는 경우 총 4가지이다.
2. 빨간색 공의 갯수, 파란색 공의 갯수를 파악하여 오른쪽 or 왼쪽 무더기에 모여있는 색깔의 공의 갯수를 빼면 오른쪽 or 왼쪽으로 옮기는 횟수가 된다.
3. 오른쪽 옮기는 경우에는 입력받은 리스트 balls를 역순으로 탐색한다.

