## Q1. 숫자를 입력 받고 3자리마다 ,를 찍어주는 함수

def make_comma(num):
    num = str(num)

    if len(num) <= 3:
        return num
    else:
        return make_comma(num[:-3]) + ',' + num[-3:]

print(make_comma(1000000000))



## Q2. 전체 글 중 특정 글자가 몇개 들어있는지 출력, 글도 txt파일로 저장

def count_word(text, word):
    f = open('test.txt', 'w')
    f.write(text)
    f.close()

    print(text.count(word))

text = """ 비극으로 끝난 일가족 실종 사건
지난 6월 29일 오전 10시 25분, 평소 한산하기만 했던 완도 송곡항엔 많은 이들이 모여 있었다.
모두 눈앞의 바다만을 바라보는 가운데, 은색 승용차 한 대가 물 위로 끌어 올려졌다. 바다 밑에 숨겨져 있던 비극이 모습을 드러내는 순간 모두가 숨을 죽였다.
전 국민이 안타깝게 느낀 일가족의 실종... 그 결말이 거기에 있었기 때문이었다.
지난 5월 24일, 경찰은 실종된 한 사람의 사진을 공개하고, 제보를 받았다. 사진의 주인공은 10살의 조 양. 실종신고를 한 사람은 가족이 아닌 조 양의 담임 선생님이었다.
부모님과 제주도 여행을 간다며 체험학습 신청서까지 제출했던 아이. 하지만 약속한 체험학습 기간이 끝났어도 조 양은 학교로 돌아오지 않았고 부모와의 연락도 되지 않았다.
그렇게 실종된 일가족의 흔적을 쫓아 경찰수사가 시작되었는데.... 안타깝게도 한 달 만에 확인된 사실은 일가족의 사망이었다.
조 양 일가족의 시신이 인양된 승용차 안에서 발견되었고, 부검 결과 3명의 가족 모두에게서 수면제 성분이 검출됐다. 부모의 동기는 경제적 문제였던 것으로 보이는 상황.
과연, 이 비극은 막을 수 없었던 걸까. 그리고 스스로 선택하지도 않았는데, 아이는 왜 그런 운명을 맞이해야만 했을까. 만일, 조 양이 살아있었다면, 우리에게 어떤 이야기를 하고 싶을까."""
count_word(text, '일가족')



## Q3.  방명록을 받아 잘못된 양식의 이름과 번호를 출력하는 함수
##      함수에 방명록을 넣으면 txt로 저장
##      010 으로 시작 / -로 구분 / - 포함 13글자

def wrong_guest_book(guest_book):
    f = open("guest_book.txt", 'w')
    f.write(guest_book)
    f.close()

    guest_book = guest_book.split("\n")
    list = []
    
    for tmp in guest_book:
        list.append(tmp.split(","))

    for tmp in list:
        if (tmp[1].find("-") == -1) or (tmp[1][0:3] != ('010') or (len(tmp[1]) != 13)):
            print("잘못 쓴 사람 : " + tmp[0] + "\n잘못 쓴 번호 : " + tmp[1] + "\n")
    

guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""
wrong_guest_book(guest_book)



## Q4.  주민등록번호를 입력하면 몇년 몇월 생, 성별을 출력하는 함수
##       -로 구분 - 포함 길이 14
##       1,3:남자 2,4:여자
##       00 ~ 21 로 시작하면 2000년 이후 출생자인지 물어볼 것 (o,x)
##       뒷자리 3,4는 00년생 이후 출생자만
##       조건 불만족시 "잘못된 번호입니다." 출력

from tabnanny import check


def check_id(num):
    check = 'x'
    bool = 1
    tmp = num.split('-')

    if (num.find("-") == -1) or len(num) != 14:
        bool = 0
    else :
        if (num[:2] >= "00") and (num[:2] <= "21"):
            check = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")
    
        if check == 'o':
            if tmp[1][:1] == 3 or tmp[1][:1] == 4:
                bool = 1
            else :
                bool = 0
    
    if bool:
        gender = "여자"
        if tmp[1][:1] == 1 or tmp[1][:1] == 3 :
            gender = "남자"

        print(tmp[0][:2] + "년 " + tmp[0][2:4] + "월 " + gender)
    else :
        print("잘못된 번호입니다.\n올바른 번호를 넣어주세요.")

a = "500629-2222222"
check_id(a)

a = "000629-2222222"
check_id(a)