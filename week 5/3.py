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