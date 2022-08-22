## Q1.  고려시대와 조선시대 왕 이름 중 고려외 조선에 모두 있는 이름을 찾는 함수
##      조건1 : 중복되는 왕 이름 출력
##      조건2 : 중복되는 왕 이름 갯수 출력

def king(korea, chosun):
    num = 0
    korea = korea.split(",")
    chosun = chosun.split(",")
    king = dict()

    for kor in korea:
        king[kor] = 1
    
    for cho in chosun:
        if king.get(cho, 0) >= 1:
            king[cho] = king[cho] + 1

    count_king = [k for (k,v) in king.items() if v >= 2]

    for tmp in count_king:
        print("조선과 고려에 모두 있는 왕 이름 : " + tmp)
        num += 1

    return num

korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"

print("조선과 고려에 모두 있는 왕 이름은 총 ", king(korea_king, chosun_king), "개 입니다.")