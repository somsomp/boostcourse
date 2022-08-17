## Q3.  방명록을 받아 잘못된 양식의 이름과 번호를 출력하는 함수
##      함수에 방명록을 넣으면 txt로 저장
##      010 으로 시작 / -로 구분 / - 포함 13글자

def wrong_guest_book(guest_book):
    f = open("guest_book.txt", 'w')
    f.write(guest_book)
    f.close()

    guest_book = guest_book.split("\n")
    list = []
    
    for tmp in guest_book:
        list.append(tmp.split(","))

    for tmp in list:
        if (tmp[1].find("-") == -1) or (tmp[1][0:3] != ('010') or (len(tmp[1]) != 13)):
            print("잘못 쓴 사람 : " + tmp[0] + "\n잘못 쓴 번호 : " + tmp[1] + "\n")
    

guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""
wrong_guest_book(guest_book)