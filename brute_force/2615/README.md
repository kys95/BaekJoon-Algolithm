# 문제

1. 검은 바둑알 or 흰 바둑알이 5개 연속으로 놓이면 이기게 된다.
2. 단, 6개이상 놓이면 오목이 아니므로 이긴 것이 아니다.
3. 검은색과 흰색이 동시에 이기거나 검은색 또는 흰색이 두 군데 이상에서 동시에 이기는 경우는 없다.



# 해결과정

1. 바둑알이 놓일 수 있는 좌표의 총 갯수는 400이하, 각 좌표에 해당하는 4가지 방향확인(오른쪽, 오른쪽 대각선 아래, 오른쪽 대각선 위, 아래), 5개의 연속된 좌표가 있는지 확인하는 경우의 수를 고려했을 때 완전탐색을 이용한다.
2. 승리했을 때 왼쪽좌표 or 위쪽 좌표를 출력해야 하므로 편의상 오른쪽, 오른쪽 대각선 아래, 오른쪽 대각선 위, 아래방향 총 4가지 방향으로 나누어 5개의 연속된 좌표가 있는지 확인한다.
3. 5개의 연속된 좌표가 있다면 6개 이상의 연속된 바둑알이 놓여있는지 확인하기 위해 끝과 끝을 한번 더 고려해준다.
4. 검은색이 이기게된다면 햐안색은 고려하지 않고 종료한다.

