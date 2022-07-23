# Q1. 컴퓨터와 함께 하는 가위바위보 게임

import random


me = int(input("가위는 1 바위는 2 보는 3 을 입력해주세요. : "))
while me not in [1, 2, 3] :
    print("잘못 입력하셨습니다. 다시 입력하세요.")
    me = int(input("가위는 1 바위는 2 보는 3 을 입력해주세요. : "))
computer = random.randint(0, 2)

print("\n<<<<< 결과 >>>>>")
print("나 : " + {1 : "가위", 2 : "바위", 3 : "보"}.get(me))
print("컴퓨터 : " + {1 : "가위", 2 : "바위", 3 : "보"}.get(me))

result = me - computer
if(result == 0) :
    print("비겼습니다.")
elif(result == -1 or result == 2) :
    print("컴퓨터가 이겼습니다.")
else :
    print("내가 이겼습니다.")


# Q2. 월급을 입력하면 연봉을 계산해주는 계산기_세전, 세후 모두 출력

salary = int(input("현재 월급은 얼마인가요? (만원단위의 숫자로 입력해주세요.)\t"))
annual_salary = salary * 12
annual_salary_tax = 0

if(annual_salary <= 1200) :
    annual_salary_tax = annual_salary * 0.94
elif(annual_salary <= 4600) :
    annual_salary_tax = annual_salary * 0.85
elif(annual_salary <= 8800) :
    annual_salary_tax = annual_salary * 0.76
elif(annual_salary <= 15000) :
    annual_salary_tax = annual_salary * 0.65
elif(annual_salary <= 30000) :
    annual_salary_tax = annual_salary * 0.62  
elif(annual_salary <= 50000) :
    annual_salary_tax = annual_salary * 0.60
else : 
    annual_salary_tax = annual_salary *0.58

annual_salary_tax = int(annual_salary_tax)

print("\n<<<<< 결과 >>>>>")
print("세전 연봉 :", annual_salary,"만원")
print("세후 연봉 :", annual_salary_tax, "만원")


# Q3. 학생 이름과 점수를 입력받아 학점을 출력하는 학점 변환기_이름, 점수, 학점 모두 출력

def grader (name, score) :
    if(score >= 95) :
        return "A+"
    elif(score >= 90) :
        return "A"
    elif(score >= 85) :
        return "B+"
    elif(score >= 80) :
        return "B"
    elif(score >= 75) :
        return "C+"
    elif(score >= 70) :
        return "C"
    elif(score >= 65) :
        return "D+"
    elif(score >= 60) :
        return "D"
    else :
        return "F"

try :
    name = input("이름을 입력하세요. : ")
    score = int(input("점수를 입력하세요. : "))

    while score > 100 :
        print("잘못된 점수 입니다. 다시 입력하세요.")
        score = int(input("점수를 입력하세요. : "))
except :
    print("===== Input Error =====")

print("\n<<<<< 결과 >>>>>")
print("이름 :", name)
print("점수 :", score)
print("학점 :", grader(name, score))


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