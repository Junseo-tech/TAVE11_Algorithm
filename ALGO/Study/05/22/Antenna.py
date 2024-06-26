'''
일직선상의 마을에 여러 채의 집이 위치해 있습니다. 이 중에서 특정 위치의 집에 특별히 한 개의 안테나를
설치하기로 결정했습니다. 효율성을 위해 안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록 설치하려고 합니다.
이때 안테나는 집이 위치한 곳에만 설치할 수 있고, 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능합니다.

집들의 위치 값이 주어질 때, 안테나를 설치할 위치를 선택하는 프로그램을 작성하세요.

예를들어 N = 4이고, 위치가 1,5,7,9 일 때를 가정하겠습니다.

이 경우 5의 위치에 설치 했을 때, 안테나로부터 모든 집 까지의 거리의 총합이 (4+0+2+4) = 10으로, 최소가 됩니다.

입력조건
- 첫째 줄에 집의 수 N이 자연수로 주어집니다. (1 <= N <= 200,000)
- 둘째 줄에 N채의 집에 위치가 공백으로 구분되어 1 이상 100,000 이하의 자연수로 주어집니다.

출력조건
- 첫째 줄에 안테나를 설치할 위치의 값을 출력ㅊ합니다. 단, 안테나를 설치할 수 있는 위치 값으로 여러개의 값이 
도출될 경우 가장 작은 값을 출력합니다.

입력 예시
4
5 1 7 9

출력예시 
5
'''

N = int(input())
dist = list(map(int, input().split()))

dist.sort()

answer = dist[(N-1)//2]

print(answer)