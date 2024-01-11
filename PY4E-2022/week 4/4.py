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