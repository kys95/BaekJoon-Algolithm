# 문제

1. 1~n일 까지 초기현금 w으로 매일 변동되는 코인 가격을 매수 or 매도 하여 최종 현금의 최댓값을 출력해라.



# 해결과정

1. 싸게 사서 비싸게 팔아야 현금의 최댓값을 구할 수 있다.
2. 매수가, 매도가를 0으로 초기화하고 상방이라면 매수가와 매도가를 입력한다. 단, 매수가가 원래부터 있었다면 매도가만 변경한다.
3. 이득은 profit = (sell - buy) * (w // buy)로서 매수하고 매도했을 때의 이득을 w에 누적합 해준다.
4. 코인 가격을 돌고 난후 매수가와 매도가가 남아있을 경우 한번 더 합해준다.