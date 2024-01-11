## Q1.  고려시대와 조선시대 왕 이름 중 고려외 조선에 모두 있는 이름을 찾는 함수
##      조건1 : 중복되는 왕 이름 출력
##      조건2 : 중복되는 왕 이름 갯수 출력

def king(korea, chosun):
    num = 0
    korea = korea.split(",")
    chosun = chosun.split(",")
    king = dict()

    for kor in korea:
        king[kor] = 1
    
    for cho in chosun:
        if king.get(cho, 0) >= 1:
            king[cho] = king[cho] + 1

    count_king = [k for (k,v) in king.items() if v >= 2]

    for tmp in count_king:
        print("조선과 고려에 모두 있는 왕 이름 : " + tmp)
        num += 1

    return num

korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"

print("조선과 고려에 모두 있는 왕 이름은 총 ", king(korea_king, chosun_king), "개 입니다.")



## Q2.  6명의 영업팀의 영업관리자가 올해 실적에 따라 보너스와 면담을 할 때 정하는 함수
##      조건 1: 보너스 대상자는 평균 실적 1, 2등
##      조건 2: 면담 대상자는 평균 실적 5, 6등
##      조건 3: 보너스 대상자의 평균 실적이 5보다 크지 않으면 보너스 대상자 제외
##      조건 4: 면담 대상자 평균 실적이 3보다 크면 면담 대상자 제외

from itertools import count


def sales_management(name, records):
    member = dict()
    i = 0
    records_list = []

    for list in records:
        record = 0
        count = 0
        for a in list:
            record += a
            count += 1
        records_list.append(record/count)

    for tmp in name:
        member[tmp] = records_list[i]
        i += 1

    members = dict(sorted(member.items(), key=lambda x: x[1], reverse=True))
    ran = [k for (k, v) in members.items()]
    
    for i in range(2):
        result = members[ran[i]]
        if result > 5:
            print("보너스 대상자 : " + ran[i])
    
    for i in range(4, 6):
        result = members[ran[i]]
        if result < 3:
            print("면담 대상자 : " + ran[i])


member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2], 
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

sales_management(member_names, member_records)



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



## Q4.  매월 상품을 많이 구매한 VIP회원에게 할인 쿠폰 제공
##      회원 정보를 출력하고 할인 쿠폰을 받을 회원이 누구인지 출력하는 함수
##      조건 1: 8회이상 구매시 vip
##      조건 2: 전화번호가 있어야 쿠폰 발급 가능
##      조건 3: 전화번호가 없으면 000-0000-0000으로 출력

def good_customer(info):
    info = info.split(",")
    custom =[]
    i = 0
    tmp_list = []

    for tmp in info:
        if i == 5:
            tmp_list.append(tmp)
            custom.append(tmp_list)
            i = 0
            tmp_list = []
        else:
            tmp_list.append(tmp)
            i += 1
    
    custom_list = []
    for tmp in custom:
        if tmp[2] == 'x':
            tmp[2] = '000-0000-0000'
        a = {'아이디':tmp[0], '나이' : tmp[1], '전화번호' : tmp[2], '성별' : tmp[3], '지역' : tmp[4], '구매횟수' : tmp[5]}
        custom_list.append(a)
    
    for tmp in custom_list:
        print("회원 정보_\n", tmp)
    
    print()
    
    for tmp in custom_list:
        if int(tmp.get('구매횟수')) >= 8 and tmp.get('전화번호') != '000-0000-0000':
            print('할인 쿠폰 받을 회원 정보 아이디 : ', tmp)

   # print(custom)

# 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"

good_customer(info)