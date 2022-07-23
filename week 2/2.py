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