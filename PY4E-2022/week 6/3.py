## Q3. 매수한 종목 이름, 수량, 매수 평균 금액이 주어지고 판매가는 따로 주어졌을 때
##     종목과 수익률만 출력, 종목별 수익률이 높은 순서대로 출력 / 소수 둘째자리까지만

def stock_profit(stocks, sells):
    stocks = stocks.split(",")
    stock = []
    for tmp in stocks:
        stock.append(tmp.split("/"))
    
    profit = []
    for i in range(len(stock)):
        tmp = (sells[i]/int(stock[i][2])-1)*100
        profit.append((tmp, stock[i][0]))

    profit.sort(reverse=True)

    for tmp in profit:
        print(f"{tmp[1]}의 수익률 {tmp[0]:.3}")

stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]

stock_profit(stocks, sells)