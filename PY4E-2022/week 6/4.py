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