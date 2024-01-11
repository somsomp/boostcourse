## Q2. 학생들의 시헙 답지와 정답지로 채점하고 점수와 등수를 출력하는 함수 생성


def grader(right, answer):
    answer_list = []
    count = 0
    score = []

    for tmp in answer:
        answer_list.append(tmp.split(","))
    
    
    for tmp in answer_list:
        count = 0
        i = 0
        for a in tmp[1]:
            #print(a, " / ", right[i])
            if int(a) == right[i]:
                count += 1
            i += 1
        score.append([count*10, tmp[0]])
    score.sort(reverse=True)
    
    i = 1
    for tmp in score:
        print("학생 : " + tmp[1] + " | 점수 : ", tmp[0], "점 | ", i, "등")
        i += 1


# 학생 답
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

grader(a, s)