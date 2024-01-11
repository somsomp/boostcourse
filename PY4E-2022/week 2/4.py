# Q4. 나이와 현금 또는 카드를 입력하면 버스 요금이 출력되는 버스 요금 계산기

def bus_fare(age, type) :
    if(age < 8 or age >= 75) :
        return "무료"
    elif(age < 14) :
        return "450원"
    elif(age < 20) :
        return {"카드" : "720원", "현금" : "1000원"}.get(type)
    else :
        return {"카드" : "1200원", "현금" : "1300원"}.get(type)

try :
    age = int(input("나이를 입력하세요. : "))
    type = input("결제 유형을 입력하세요. : ")

    while type not in ["카드", "현금"]:
        print("잘못된 결제 유형 입니다. 다시 입력하세요.")
    type = input("결제 유형을 입력하세요. : ")
except :
    print("===== Input Error =====")

print("\n<<<<< 결과 >>>>>")
print("나    이 :", age)
print("지불유형 :", type)
print("버스요금 :", bus_fare(age, type))