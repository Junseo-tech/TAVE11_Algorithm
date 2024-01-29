def solution(answers):
    answer = []
    score_1,score_2,score_3 = 0,0,0 
    student_1 = [1,2,3,4,5]
    student_2 = [2,1,2,3,2,4,2,5]
    student_3 = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        if answers[i] == student_1[i % len(student_1)]:
            score_1 += 1
        if answers[i] == student_2[i % len(student_2)]:
            score_2 += 1
        if answers[i] == student_3[i % len(student_3)]:
            score_3 += 1

    # 점수 높으면 학생이 리스트에 들어가야 함
    max_score = max(score_1,score_2,score_3)
    answer = [idx + 1 for idx,score in enumerate([score_1, score_2, score_3]) if score == max_score]
    # for idx, score in enumerate([score_1, score_2, score_3]):
    #     if score == max_score:
    #         answer.append(idx + 1)
    return answer

answers = [1,3,2,4,2]
print(solution(answers))