import sys
input = sys.stdin.readline

A,B = map(int, input().split())

if A > B:
    print(">")

if A < B:
    print("<")

if A == B:
    print("==")