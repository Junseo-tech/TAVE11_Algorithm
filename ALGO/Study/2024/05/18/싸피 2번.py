'''
N명의 사람이 배치고사를 보고 받은 점수들이 있다.

이 사람들을 상, 중, 하 3개의 그룹으로 나누려고 한다. 상 그룹에 속한 사람들의 점수는 모두 중 그룹에 속한 사람들의 점수보다 높아야 하며, 중 그룹에 속한 사람들의 점수는 모두 하 그룹에 속한 사람들의 점수보다 높아야 한다.



상, 중, 하 그룹 모두 최소 1명의 사람이 있어야 한다.

중 그룹에는 최소 A명, 최대 B명의 사람이 있도록 하고 싶다.

중 그룹에 넣을 수 있는 최대의 인원을 계산하는 프로그램을 작성하라.

조건에 맞도록 그룹을 나누는 방법이 존재하는 경우만 테스트케이스로 주어진다.



예를 들어 N = 6, A = 1, B = 3이며,

6명의 점수가 각각 4, 3, 2, 3, 2, 1이라고 하자.

중 그룹에 2점을 받은 사람들만 넣는 경우, 중 그룹은 2명이 되고 기준을 만족한다

중 그룹에 3점을 받은 사람들만 넣는 경우에도 중 그룹은 2명이 되고 만족한다.

그러나 2점과 3점을 받은 사람들을 모두 중 그룹에 넣는 경우 4명이 되어 기준을 만족하지 못한다.




따라서, 이 경우의 답은 2이다.



[제약사항]

1.     N은 6 이상 500 이하이다. (6 ≤ N ≤ 500)

2.     1 ≤ A ≤ B < N-1이 성립한다.

3.     각 점수는 1 이상 1,000 이하의 정수이다.

4.     조건을 모두 만족하는 것이 불가능한 경우는 주어지지 않는다.



[입력]

가장 첫 줄에는 테스트 케이스의 총 수가 주어진다.

각 테스트 케이스의 첫 줄에는 N, A, B 세개의 정수 값이 공백을 사이에 두고 주어진다.

다음 줄에 N명 각각의 점수가 주어진다.



[출력]

테스트 케이스 개수만큼 T 개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.

각 줄은 “#t”로 시작하고 공백을 하나 둔 다음 정답을 출력한다. ( t는 1부터 시작하는 테스트 케이스의 번호이다. )

출력해야 할 정답은 중 그룹에, 넣을 수 있는 최대 인원수 이다.



[입력 예]

3                               // 테스트 케이스의 수
6 1 3                          // N = 6, A = 1, B = 3 테스트 케이스 #1
4 3 2 3 2 1
6 3 4                          // N = 6, 테스트 케이스 #2
1 2 3 4 5 6
6 1 4                          // N = 6, 테스트 케이스 #3
10 10 9 10 3 3


[출력 예]

#1 2
#2 4
#3 1

'''
# 12시 16분 시작 -> 12시 29분 끝
import sys
input = sys.stdin.readline
T = int(input())

for t in range(1, T+1):
    N, A, B = map(int, input().split()) # 6 1 3
    grade_list = list(map(int, input().split()))
    grade = {}
    for i in range(N):
        grade[grade_list[i]] = grade.get(grade_list[i], 0) + 1
    grades = sorted(grade.items(), key = lambda x : x[0], reverse= True) # 튜플 형태 반환 [(4,1), (3,2), (2,2), (1,1)]
    count = 0
    for i in range(1,len(grades)-1):
        if count < B:
            count += grades[i][1]
        if count > B:
            count -= grades[i-1][1]

    print(f"#{t} {count}")

