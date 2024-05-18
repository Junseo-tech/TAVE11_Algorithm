'''
어떤 가게에서 N개의 물건을 사려고 한다.

각 물건의 가격이 주어진다. 이 가게는 1+1 제도를 운영한다.

1+1제도에서는 어떤 물건을 하나 사면 다른 물건을 하나 무료로 준다.

단, 무료로 주는 물건의 조건은 돈을 내고 산 물건보다 가격이 낮아야 한다.

이 조건에 맞는 물건이 없는 경우 무료로 주는 물건은 없다.

철수는 다음과 같은 작전을 물건이 떨어질 때까지 반복하기로 했다.


1.     현재 있는 물건들 중 가장 가격이 비싼 것을 산다.

2.     무료로 받을 수 있는 물건이 있는 경우 가능한 가장 비싼 것을 받는다.


N개의 물건의 가격이 주어질 때 철수가 모든 물건을 사는 비용을 계산하는 프로그램을 작성하라.


예를 들어, N = 4이고 물건들의 가격이 각각 5, 3, 4, 3인 경우를 생각하자.

작전에 따라 가격이 5인 물건을 사고 가격이 4인 물건을 무료로 받는다.

남은 두개의 물건은 1+1 조건에 맞지 않아 가격을 지불하고 사야 한다.

따라서 총 비용은 5+3+3 = 11이다.



[제약사항]

1.     물건의 개수 N은 1 이상 500 이하이다. (1 ≤ N ≤ 500)

2.     물건의 가격은 1 이상 1,000 이하의 정수이다.



[입력]

가장 첫 줄에는 테스트 케이스의 총 수가 주어진다.

그 다음 줄부터 각 테스트 케이스가 주어지며, 각 테스트 케이스는 2 줄로 구성된다. 각

 테스트 케이스의 첫 줄에는 N이 주어진다. 다음 줄에는 물건들의 가격 N개가 주어진다.



[출력]

출력의 각 줄은 ‘#x’로 시작하고, 공백을 한 칸 둔 다음 모든 물건을 사는데 필요한 비용을 출력한다. 단, x는 테스트 케이스의 번호이다.



[입력 예]

3                    // 테스트 케이스의 수

4                          // N = 4, 테스트 케이스 #1

5 3 4 3

4                          // N = 4, 테스트 케이스 #2

1 2 3 4

4                          // N = 4, 테스트 케이스 #3

5 2 5 1



[출력 예]

#1 11

#2 6

#3 10


'''
import sys
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N = int(input())
    goods = list(map(int, input().split()))
    goods.sort(reverse=True)
    price = goods[0]
    price_count = 1
    service = 0
    if goods[0] > goods[1]:
        service = goods[1]
        price_count -= 1
    else:
        price += goods[1]
        price_count += 1

    for i in range(2, N): # 4 3 2 1         5 4 3 3           5 5 2 1
        if service > 0 and price_count == 0: # 서비스로 제공 받은 것이 있
            price += goods[i]
            price_count += 1
            service = 0
        else: # 서비스로 제공 받은 것이 없다
            if goods[i-1] > goods[i] and price_count > 0:
                service = goods[i]
                price_count -= 1
            if goods[i-1] == goods[i]:
                price_count += 1
                price += goods[i]

    print(f"#{t} {price}")