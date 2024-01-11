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