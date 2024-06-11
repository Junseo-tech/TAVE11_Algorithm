import sys
input = sys.stdin.readline

N,M,x,y,K = map(int, input().split())
# N : 세로, M : 가로, x,y : 좌표, K : 명령의 개수
maps = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

