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