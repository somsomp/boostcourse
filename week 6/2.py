## Q2.  6명의 영업팀의 영업관리자가 올해 실적에 따라 보너스와 면담을 할 때 정하는 함수
##      조건 1: 보너스 대상자는 평균 실적 1, 2등
##      조건 2: 면담 대상자는 평균 실적 5, 6등
##      조건 3: 보너스 대상자의 평균 실적이 5보다 크지 않으면 보너스 대상자 제외
##      조건 4: 면담 대상자 평균 실적이 3보다 크면 면담 대상자 제외

from itertools import count


def sales_management(name, records):
    member = dict()
    i = 0
    records_list = []

    for list in records:
        record = 0
        count = 0
        for a in list:
            record += a
            count += 1
        records_list.append(record/count)

    for tmp in name:
        member[tmp] = records_list[i]
        i += 1

    members = dict(sorted(member.items(), key=lambda x: x[1], reverse=True))
    ran = [k for (k, v) in members.items()]
    
    for i in range(2):
        result = members[ran[i]]
        if result > 5:
            print("보너스 대상자 : " + ran[i])
    
    for i in range(4, 6):
        result = members[ran[i]]
        if result < 3:
            print("면담 대상자 : " + ran[i])


member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2], 
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

sales_management(member_names, member_records)