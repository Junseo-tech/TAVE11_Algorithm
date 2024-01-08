# import sys

# input = sys.stdin.readline

# S,P = map(int, input().split())
# DNA = input().strip()
# base_dict = {"A": 0 , "C": 0, "G": 0, "T": 0}

# numbers = list(map(int, input().split()))

# for i,key in enumerate(base_dict):
#     base_dict[key] = numbers[i]

# base_count = sum(base_dict.values())
# result = 0

# if base_count < P:
#     print(result)
# else:
#     for i in range(S-P+1):
#         sequence = DNA[i : i+P]
#         for base in sequence:
#             base_dict[base] -= 1
#             if base_dict[base] < 0:
#                 break
#         else:
#             result += 1
#     print(result)
# 위 는 정답 값을 건드리기 때문에 안된다.




