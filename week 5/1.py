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