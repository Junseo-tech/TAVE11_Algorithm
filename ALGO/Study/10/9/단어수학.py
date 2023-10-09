'''
민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.

단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 
이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 
같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.

예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 
두 수의 합은 99437이 되어서 최대가 될 것이다.

N개의 단어가 주어졌을 때, 
그 수의 합을 최대로 만드는 프로그램을 작성하시오.

입력
----
첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다. 
둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다. 단어는 알파벳 대문자로만 이루어져있다. 
모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8이다. 
서로 다른 문자는 서로 다른 숫자를 나타낸다.

출력
----
첫째 줄에 주어진 단어의 합의 최댓값을 출력한다.

예제 입력 1
---------
2
AAA
AAA

예제 출력 1
---------
1998

'''
import sys
input = sys.stdin.readline

N = int(input())
dict = {}

word = []
for _ in range(N):
    word.append(list(input().strip()))
# word -> [['G', 'C', 'F'], ['A', 'C', 'D', 'E', 'B']]

for i in range(N): # N 만큼 word 돌아감
    for j in enumerate(word[i]):
      
    # 자릿 수 만큼 10 제곱형태 배당 시켜야 함
    # 만약 전에 딕셔너리에 같은 것이 있으면 더해주고, 없으면 새로운 자릿수를 배당해야 함
        if j[1] in dict:
            dict[j[1]] += 10 ** (len(word[i]) - (j[0]+1))    
        else:
            dict[j[1]] = 10 ** (len(word[i]) - (j[0]+1))

# 빈도 수 대로 높은 수 할당하기
answer = list(dict.values())
answer.sort(reverse=True)

cnt = 9
real_answer = 0

for i in range(len(answer)):
  real_answer += answer[i] * cnt
  cnt -= 1

print(real_answer)
  


  