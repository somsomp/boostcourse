## Q1. 숫자를 입력 받고 3자리마다 ,를 찍어주는 함수

def make_comma(num):
    num = str(num)

    if len(num) <= 3:
        return num
    else:
        return make_comma(num[:-3]) + ',' + num[-3:]

print(make_comma(1000000000))