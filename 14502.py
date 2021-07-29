# 크기 : n x m 
# 바이러스는 상하좌우로 움직임
# 0 : 빈칸 , 1 : 벽 , 2: 바이러스
# 벽은 꼭 3개를 세워야 함

from itertools import combinations
from collections import deque
import sys

n,m = map(int, sys.stdin.readline().split())

maps = []
virus = deque()
empty = []

for i in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))
    for idx,j in enumerate (maps[i]):
        if j == 2:
            virus.append([i,idx])
        elif j == 0:
            empty.append([i,idx])

def FindMax(obj):
    flag = False
    cnt = 0 # 나중에 세어진 만큼 len(empty) 에서 빼줄거임

    for y,x in obj: # 임의로 뽑은 빈 칸 세곳에 벽을 설치
        maps[y][x] = 1

    # virus 를 시작점으로 하고 4방향 탐색 , 2로 바꿔 줌 -> maps 의 끝까지 가기전에 벽 or 바이러스가 먼저 나오면 통과
    # 예외로 virus 시작점이 최외각인 경우 탐색 방향을 줄여줘야 함
    # maps 의 끝까지 탐색하는 중 벽이 안나오면 flag = True
    # 맨 마지막에 flag = False 이면 이 맵에서의 0 의 갯수 return

    # virus 를 deque 로 만들고 deque 가 전부 빌때까지 반복해야할것 같음.
    while virus:
        y,x = virus.popleft()

        for j in range(y-1, -1, -1):
            if maps[j][x] == 1 or maps[j][x] == 2:
                break
            else:
                maps[j][x] = 2
                cnt += 1
                virus.append([j,x])
                empty.pop() # 빈칸 하나 제거
        for j in range(y+1, n, 1):
            if maps[j][x] == 1 or maps[j][x] == 2:
                break
            else:
                maps[j][x] = 2
                cnt += 1
                virus.append([j,x])
                empty.pop()
        for i in range(x-1, -1, -1):
            if maps[y][i] == 1 or maps[y][i] == 2:
                break
            else:
                maps[y][i] = 2
                cnt += 1
                virus.append([y,i])
                empty.pop()
        for i in range(x+1, m, 1):
            if maps[y][i] == 1 or maps[y][i] == 2:
                break
            else:
                maps[y][i] = 2
                cnt += 1
                virus.append([y,i])
                empty.pop()

    tmp = len(empty) - cnt
    for _ in range(cnt):
        empty.append([0,0])

    # if flag == False:
    #     tmp = len(empty) - cnt
    # else:
    #     tmp = 0

    for y,x in obj: # 확인이 끝나고 난 후
        maps[y][x] = 0 # 원래대로 돌려 놓는다.

    if tmp > 0:
        return tmp
    else:
        return 0
    
score = []
for obj in combinations(empty,3):
    tmp_score = FindMax(obj)
    if tmp_score != 0:
        score.append(tmp_score)

print("maps : ",maps,"\nvirus : ",virus,"\nempty : ",empty)