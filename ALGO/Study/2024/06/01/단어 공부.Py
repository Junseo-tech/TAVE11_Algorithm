word = input().strip()
word = word.upper()
word_dict = {}

if len(word) == 1:
    print(word)
    exit()

for w in word:
    word_dict[w] = word_dict.get(w, 0) + 1

words = sorted(word_dict.items(), key=lambda x:x[1], reverse=True)

m = words[0][1]

for i in range(1, len(words)):
    if words[i][1] == m:
        print("?")
        exit()

print(words[0][0])