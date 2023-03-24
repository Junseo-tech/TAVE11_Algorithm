'''
당신은 음식점의 계산을 도와주는 점원입니다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원,
10원짜리 동전이 무한히 존재한다고 가정합니다. 손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러 주어야 할 
동전의 최소 개수를 구하세요. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수입니다.

'''

N = int(input())

change_list = [500, 100, 50, 10]
change_num = 0

while(N != 0):
    for i in range(len(change_list)):
        if N > change_list[i]:
            N = N - change_list[i]
            change_num += 1

        elif N < change_list[i]:
           i = i+1

        else:
            N = N - change_list[i]
            change_num += 1

print(change_num);

        


