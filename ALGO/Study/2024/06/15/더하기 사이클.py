a = int(input())
num = a
count = 0

while True:
    x = num//10
    b = num%10
    c = (x+b)%10
    num = (b*10) + c
    count += 1 
    if(num == a):
        break
print(count)