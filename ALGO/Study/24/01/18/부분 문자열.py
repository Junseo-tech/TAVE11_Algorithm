import sys



# for line in input:
#     s,t = line.split()

# if any(''.join(i) == s for i in combinations(t, len(s))):
#     print("Yes")
# else:
#     print("No") 
# 순서대로라는 조건이 있는데 가능한 조합 모두를 고려하다보니 시간초과

count = 0


def findSub(s,t):
    global count
    for char in t :
        if s[count] == char:
            count += 1
            if count == len(s) :
                return "Yes"
    else:
        return "No"

while True :
    try:
        input = sys.stdin.readline().rstrip()
        if not input :
            break
        count = 0
        s,t = input.split()
        print(findSub(s,t))
    except: break
