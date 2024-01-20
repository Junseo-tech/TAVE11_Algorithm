import sys
input = sys.stdin.readline

code = input().strip()
N = int(input())
dict_word = []

for _ in range(N):
    dict_word.append(input().strip())

for i in range(26):
    decoded_message = ""
    for c in code:
        decoded_message += chr(((ord(c)-97+i)%26)+97)
    if any(word in decoded_message for word in dict_word):
        print(decoded_message)
        

