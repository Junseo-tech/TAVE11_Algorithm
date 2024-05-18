'''
N개의 화분이 좌우로 놓여 있다.

두 가지의 비료가 있고 각각이 하나의 기계에 담겨 있다.

두 기계를 들고 왼쪽부터 각 화분에 비료를 주려고 한다.

한 화분에는 하나의 비료만 준다. 각 화분에 대해서 첫 번째 비료를 주었을 때 해당 화분의 식물이 자라는 높이와 두 번째 비료를 주었을 때 자라는 높이를 알고 있다고 한다.

단, 한 화분에 준 비료를 바로 오른쪽 화분에 또 주는 경우 기계의 펌프가 약해져서 식물이 원래 자라야 할 높이보다 P 만큼 덜 자라게 된다.

펌프가 약해지는 정도는 누적이 되지 않는다.


예를 들어, 첫 번째 화분에 비료를 주고,

두 번째와 세 번째 화분에도 같은 비료를 준 경우 두 번째 세 번째 화분의 식물은 동일하게 P 만큼 덜 자라게 된다.

전체 화분의 식물이 자라는 높이의 합이 가장 큰 경우를 찾고,

그 때의 높이의 합을 출력하는 프로그램을 작성하라

예를 들어 N = 4, P = 2이며, 첫번째 비료를 주었을 때 자라는 높이가 왼쪽부터 각각 4, 2, 6, 4이고, 두 번째 비료를 주었을 때 자라는 높이가 왼쪽부터 각각 5, 6, 4, 1이라고 하자.

제일 왼쪽 화분에 첫번째 비료 (높이 4), 다음 화분에 두번째 비료 (높이 6), 다음 화분에 첫번째 비료 (높이 6), 마지막 화분에 첫번째 비료 (높이 2), 이렇게 비료를 주는 경우가 가장 높은 합을 얻는 방법이다.


[제약사항]

1.     N은 4 이상 20 이하이다. (4 ≤ N ≤ 20)

2.     각 화분의 자라는 높이 값은 모두 1 이상 100 이하의 정수이다.

3.     P의 값은 1 이상 30 이하의 정수이다.



[입력]

가장 첫 줄에는 테스트 케이스의 총 수가 주어진다.

그 다음 줄부터 각 테스트 케이스가 주어지며, 각 테스트 케이스는 3줄로 구성된다.

각 테스트 케이스의 첫 줄에는 N과 P의 값이 주어진다.

다음 줄에는 각 화분에 첫번째 비료를 주었을 때 자라는 높이가 왼쪽 화분부터 순서대로 주어진다. 다음 줄에 두번째 비료를 주었을 때 자라는 높이가 동일한 방식으로 주어진다.



[출력]

출력의 각 줄은 ‘#x’로 시작하고, 공백을 한 칸 두고 가장 높은 때의 높이 합을 출력한다. 단, x는 테스트 케이스의 번호이다.



[입력 예]

3                    // 테스트 케이스의 수

4 2                          // N = 4, 테스트 케이스 #1

4 2 6 4

5 6 4 1

4 1                          // N = 4, 테스트 케이스 #2

1 2 3 4

4 3 2 1

6 2                          // N = 6, 테스트 케이스 #3

5 5 5 5 5 5

6 6 6 6 6 6


[출력 예]

#1 18

#2 12

#3 33

'''
import sys
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N, P = map(int, input().split())
    one = list(map(int, input().split()))
    two = list(map(int, input().split()))
    dp = [0 for _ in range(N+1)]
    one_flag = False
    two_flag = False
    for i in range(1, N):
        num = 0
        num_1, num_2, num_3, num_4 = 0, 0, 0, 0
        if i == 1:
            num = max(one[i-1] + one[i] - P, one[i-1] + two[i], two[i-1] + two[i] - P)
            dp[i] = max(dp[i], dp[i-1] + num)
            if num == one[i-1] + one[i] - P or num == one[i-1] + two[i]:
                one_flag = True
            if num == two[i-1] + two[i] - P:
                two_flag = True
        else:
            if one_flag:
                num_1 = one[i] - P
                num_2 = two[i]
            if two_flag:
                num_3 = two[i] - P
                num_4 = one[i]
            #print(num_1, num_2, num_3, num_4)
            num = max(num_1, num_2, num_3, num_4)
            #print(num)
            if num == num_1:
                one_flag = True
                two_flag = False
            if num == num_2:
                two_flag = True
                one_flag = False
            if num == num_3:
                two_flag = True
                one_flag = False
            if num == num_4:
                one_flag = True
                two_flag = False
            dp[i] = max(dp[i], dp[i-1] + num)

    print(f"#{t} {dp[N-1]}")