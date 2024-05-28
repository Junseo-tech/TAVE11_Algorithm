bryan = input().strip()
ppap_list = []

# PPPAPAP
# PPAPAPP

for char in bryan:
    ppap_list.append(char)
    if len(ppap_list) >= 4 and ppap_list[-4:] == ['P','P','A','P']:
        # ppap_list = ppap_list[:-4] # 뒤에 4개 빼고 앞에꺼만으로 재정의
        # ppap_list.append('P')
        ppap_list[-4:] = ['P']

if ppap_list == ['P','P','A','P'] or ppap_list == ['P']:
    print("PPAP")
else:
    print("NP")

