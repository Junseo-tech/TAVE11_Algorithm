import sys
input = sys.stdin.readline
N,d,k,c = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input().strip()))
choice = [0] * (d + 1) # 쿠폰 번호 1부터 30
max_count = 0
is_c = False

for i in range(k): # 처음 k개의 초밥을 선택해서 중복되지 않은 수만 더해주기
    choice[sushi[i]] += 1
    if choice[sushi[i]] == 1:
        max_count += 1
    if sushi[i] == c:
        is_c = True


# 여기서 부터 슬라이딩 윈도우 알고리즘 적용해야 함
# 더하고, max값 갱신하고, 더하고 맥스값 갱신하고
# 예제 1번이면 이제 7 9 30 2 7.. 이면 7 제외 9 30 2 7 이렇게 dk tlqkf
        
if is_c == False:
    max_count += 1
    is_c = True

result = max_count
for i in range(1,N):
    choice[sushi[i-1]] -= 1
    if sushi[i-1] == c :
        is_c = False
    if choice[sushi[i-1]] == 0:
        max_count -= 1
    # 뒤에꺼 추가
    choice[sushi[(k+i-1) % N]] += 1
    if choice[sushi[(k+i-1) % N]] == 1 :
        max_count += 1
    if not is_c and c not in sushi[i:(i+k-1) % N]:
        print(i, choice[7],is_c, max_count)
        is_c = True
        max_count += 1
    result = max(result, max_count)

print(result)

