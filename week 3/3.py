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