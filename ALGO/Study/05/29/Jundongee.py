'''
H-ALGO 회원인 한동이는 공부하는것을 좋아하지 않는다. 
하지만 약삭빠르게도 한동이는 공부도 하지 않으면서 어려운 시험을 통과하고 싶어한다.

그러던 와중 어느 날, 한동이의 동기가 한동이에게 선배들 중 누군가가 시험의 답을 알고있다는 꿀정보를 알려주었다. 

하지만 안타깝게도 그 정보는 사실이 아니어서 선배들조차도 정답은 알지 못하고 
다른 누군가가 알고 있을거 같다는 정보만 알고 있는 것이었다.

한동이는 택민이에게 시험 정답을 물어보았다. 택민이는 답을 모른다고 했지만 택민이는 상준이가 답을 알고 있을 것 같다고 하였다. 
그 후, 한동이는 상준이에게 물어보고 그리고...

어느 순간 한동이는 아무리 이걸 해도 자신에게 도움이 되지 않는것을 깨닫고 굉장히 슬퍼졌다. 
하지만 그는 이걸 함으로써 많은 선배들과 인맥을 쌓을 수 있고, 이게 언젠가 큰 도움이 될 것이라는 것을 깨달았다!

당신의 목표는 한동이가 한 사람에게만 시험문제를 물어볼 수 있다고 할 때, 
최대한 많은 선배들을 만날 수 있게 하기 위해서 누구에게 시험문제를 물어 볼 것인지를 알려주는 것이다.

입력
입력의 첫 줄에는 정수 N이 주어진다. N은 2이상 1000 이하의 자연수이다. 
선배들은 1부터 N까지 번호지어져 있다.

다음 N줄에 하나의 숫자가 주어진다. 
첫 번째 줄은 첫 번째 선배의 대답이고 두 번째 줄은 두 번째 선배의 대답이다.
이렇게 N번째 선배의 대답까지 입력이 주어진다.

출력
첫째 줄에 한동이가 물어봐야 할 선배의 번호를 출력한다. 
하나 이상의 정답이 있다면 번호가 작은 선배를 출력한다. 

'''

N = int(input())

senior = [0]
result = [0]

for i in range(1, N+1):
    senior.append(int(input()))

def dfs(start):
    visited[start] = True
    if not visited[senior[start]]:
        dfs(senior[start])

for i in range(1, N+1):
    visited = [0] * (N + 1) # N+1 만큼 기록 해야 하니까
    dfs(i)
    result.append(visited.count(True))

print(result.index(max(result)))



    
    


