## Q1.  숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수를 만들어봅시다.
##      조건 1: 홀 수 번째만 출력 / 조건 2: 값이 50이하만 출력

number = int(input("출력하고 싶은 단은? "))
for n in range (1, 11, 2):
    if number * n <= 50 :
        print(number, " * ", n, " = ", number*n)
