## Q1.  베스킨라빈스31 게임
##      조건 1: 나의 턴에서는 숫자 직접 입력 space로 구분
##      조건 2: 한 턴에 !3번의 숫자만
##      조건 3: 무조건 1씩만 증가
##      조건이 안 맞으면 다시 입력

import random


print("베스킨라빈스 31 게임")
print("-------------------")
num = []
bool = 1
last = 0

while len(num) < 31:
    list = []
    if bool == 1 :
        me = input("My turn = ")
        list = me.split(" ")
    else :
        computer = random.randint(1,3)
        for i in range (1, computer + 1):
            list.append(last + i)
        print("컴퓨터 : ", list)

    length = len(list)
    first = int(list[0])
    if bool == 1:
        if length > 3 or last != first-1 or int(list[-1]) != first+length-1:
            print("잘못 입력했습니다. 다시 입력하세요.")
            continue

    num = num + list
    last = int(num[-1])
    bool *= -1
    print("현재 숫자 : ", last)

if bool == -1:
    print("lose!")
else:
    print("win!!")



## Q2. 학생들의 시헙 답지와 정답지로 채점하고 점수와 등수를 출력하는 함수 생성


def grader(right, answer):
    answer_list = []
    count = 0
    score = []

    for tmp in answer:
        answer_list.append(tmp.split(","))
    
    
    for tmp in answer_list:
        count = 0
        i = 0
        for a in tmp[1]:
            #print(a, " / ", right[i])
            if int(a) == right[i]:
                count += 1
            i += 1
        score.append([count*10, tmp[0]])
    score.sort(reverse=True)
    
    i = 1
    for tmp in score:
        print("학생 : " + tmp[1] + " | 점수 : ", tmp[0], "점 | ", i, "등")
        i += 1


# 학생 답
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

grader(a, s)



## Q3.  숫자 맞추기 컴퓨터가 지정한 임의의 숫자 3개를 맞추는 게임
##      조건 1: 0~100 중 숫자 3개 중복 불가
##      조건 2: 5, 10회 정답을 못 맞추면 최솟값, 최대값 힌트 제공
##      조건 3: 정답일 때 최소인지 중간인지 최대인지 출력


from itertools import count
import random


def guess_numbers():
    numbers = []
    number = random.randint(0, 100)
    score = 0
    count = 1
    list = []

    for i in range(3):
        while number in numbers:
            number = random.randint(0, 100)
        numbers.append(number)
    
    numbers.sort()
    while score != 3:
        print(count, "차 시도")
        answer = int(input("0 ~ 100 사이 숫자를 입력하세요. : "))

        if answer < 0 or answer > 100:
            print("\n잘못 입력하셨습니다. 다시 입력하세요.\n")
            continue

        if answer in numbers:
            score += 1

            if numbers.index(answer) == 0:
                print("정답입니다! ", answer,"은 최솟값입니다.")
            elif numbers.index(answer) == 1:
                print("정답입니다! ", answer,"은 중간값입니다.")
            elif numbers.index(answer) == 2:
                print("정답입니다! ", answer,"은 최댓값입니다.")
        else:
            if answer in list:
                print("이미 예측에 사용한 숫자입니다.")
            else:
                print(answer, "은 없습니다.")
            
            if (count == 5) or (count == 10):
                if numbers[0] > answer:
                    print(answer, "은 최솟값보다 작습니다.")
                elif numbers[0] < answer:
                    print(answer, "은 최솟값보다 큽니다.")
                elif numbers[2] > answer:
                    print(answer, "은 최댓값보다 작습니다.")
                elif numbers[2] < answer:
                    print(answer, "은 최댓값보다 큽니다.")
            
        count += 1
        list.append(answer)
        print()

    print("게임 종료 ", count, "번 시도만에 예측 성공했습니다.")

guess_numbers()



## Q4.  입력 받은 날짜의 100일 뒤가 몇월 몇일인지 계산해주는 함수
##      조건 1: 오늘부터 1일
##      조건 2: 몇년도인지 윤년 구분 없이 무조건 28일

def after_100(m,d,date):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["월", "화", "수", "목", "금", "토", "일"]
    
    print(m, "월 ", d, "일 " + date + "요일 100일 뒤  ->")

    d += 99

    while True:
        d = d - month[m-1]
        m += 1

        if d < month[m-1] :
            break

    tmp = week.index(date)
    print(m, "월 ", d, "일 " + week[tmp+1] + "요일")


after_100(6, 21, "월")