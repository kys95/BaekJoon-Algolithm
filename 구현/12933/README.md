# 문제
1. 오리의 울음소리는 "quack"이다.
2. 여러 마리의 오리의 울음 소리가 합쳐질 경우 "quqacukqauackck"처럼 문자가 뒤섞일 수 있다. 단, 각 오리는 "quack"순서에 맞추어 운다.
3. 오르의 울음 소리 문자열이 주어질 때 오리의 최소 개수를 구해라.
4. 오리의 울음 소리가 올바르지 않다면 -1을 출력해라.



# 해결과정
1. 오리 울음 소리 원소들을 "quack"과 일대일 비교해 나가면서 방문한다.
2. 오리의 울음 소리 문자열이 비정상적인 경우는 문자열 길이가 5의 배수가 아닌경우, 문자열이 'q'로 시작하지 않는 경우, 방문하지 않은경우, 오리
  개수가 0인 경우이다. -> 앞의 두 경우는 if문을 통해 미리 확인하고 해당하면 sys.exit()처리
3. 오리 울음 소리 문자열 길이와 같은 방문리스트를 False로 초기화 하여 생성한다.
4. 입력 받은 문자열을 순서대로 for문을 통해 방문하지 않고 'q'인 경우 solve()함수를 호출한다.
5. solve()함수에서는 'q'로 시작되는 인덱스부터 끝까지 "quack"과 비교한다. 즉, 입력 받은 문자열에서 "quack"을 순서대로 찾는 것이다.
   중복가능하므로 'k"까지 찾았어도 다시 'q'부터 시작하여 'q'까지 찾는다.->오리 한마리의 울음으로 처리
6. 입력 받은 문자열을 순서대로 for문을 통해 확인한 후 오리 개수가 0이거나 방문리스트에 False가 남아있다면 -1을 출력하고 그렇지 않다면 
   오리 개수 cnt를 출력한다.