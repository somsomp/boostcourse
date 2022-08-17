## Q1.  숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수를 만들어봅시다.
##      조건 1: 홀 수 번째만 출력 / 조건 2: 값이 50이하만 출력

number = int(input("출력하고 싶은 단은? "))
for n in range (1, 11, 2):
    if number * n <= 50 :
        print(number, " * ", n, " = ", number*n)



## Q2.  가위바위보 업그레이드 버전 함수
##      조건 1: 게임을 몇판 진행할 것인지 입력
##      조건 2: 0, 1, 2, 가위, 바위, 보 정해진 조건 이외 다른 것 입력시 재입력
##      조건 3: 게임 종료 후 총 전적 출력

import random

def game(com, me):
    list = {0:"가위", 1:"바위", 2:"보"}
    result = com - me
    if result == 0:
        print("\n컴퓨터 : " + list.get(com) + " / 나 : " + list.get(me) + " / 결과 : 무승부 입니다.\n")
        return 0
    elif result == -1 or result == 2:
        print("\n컴퓨터 : " + list.get(com) + " 나 : " + list.get(me) + " / 결과 : 이겼습니다.\n")
        return 1
    elif result == 1 or result == -2:
        print("\n컴퓨터 : " + list.get(com) + " 나 : " + list.get(me) + " / 결과 : 졌습니다.\n")
        return 2

def me():
    me = input("해당하는 숫자 혹은 글자를 입력해주세요 : ")

    while me not in ["0", "1", "2", "가위", "바위", "보"]:
        print("\n잘못 입력하셨습니다. 다시 입력하세요.")
        me = input("해당하는 숫자 혹은 글자를 입력해주세요 : ")

    if (me == "가위") or (me == "0"):
        me = 0
    elif (me == "바위") or (me == "1"):
        me = 1
    elif (me == "보") or (me == "2"):
        me = 2

    return me

def result(num):
    total = [0, 0, 0]
    for i in range(num):
        print("\n0: 가위, 1:바위, 2:보 입니다.")
        com = com = random.randint(0, 2)
        my = me()

        tmp = game(com, my)

        total[tmp] = total[tmp] + 1
    return total


number = int(input("컴퓨터와 가위바위보 몇 판을 할지 입력해주세요 : "))
score = result(number)

print("가위바위보 총 전적")
print("무승부 : ", score[0])
print("패 : ", score[2])
print("승 : ", score[1])



## Q3.  2개의 숫자를 입력 그 사이의 짝수만 출력하고 중앙값을 출력하는 함수
##      중앙값이 홀 수이면 출력하지 않음


def find_even_number(n, m):
    numbers = [i for i in range(n, m+1)]
    middle = numbers[int(len(numbers)/2)]
    if middle%2 == 0:
        print("중앙값 : " , middle)

    list = []
    for i in numbers:
        if i%2 == 0:
            list.append(i)
    print("짝수 : ", list)

n = int(input("첫 번째 수 : "))
m =  int(input("두 번째 수 : "))
find_even_number(n,m)



## Q4. 2개의 숫자를 입력 그 사이의 소수가 몇 개인지 출력하는 함수

def coun_prime_number(n, m):
    numbers = [i for i in range(n, m+1)]
    count = 0

    for i in numbers:
        tmp = 0
        if i > 3:
            for j in range(2, i+1):
                if i%j == 0:
                    tmp += 1
        
        if tmp == 0:
            count += 1
    
    return count


n = int(input("첫 번째 수 : "))
m =  int(input("두 번째 수 : "))
print("소수의 총 갯수 : ", coun_prime_number(n, m))