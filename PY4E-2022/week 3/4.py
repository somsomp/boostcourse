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