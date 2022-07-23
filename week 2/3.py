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