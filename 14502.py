# 크기 : n x m 
# 바이러스는 상하좌우로 움직임
# 0 : 빈칸 , 1 : 벽 , 2: 바이러스
# 벽은 꼭 3개를 세워야 함

from itertools import combinations
from collections import deque
import copy
import sys

n, m = map(int, sys.stdin.readline().split())

cnt = []

maps = []
empty = []
virus = []
for i in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))
    for idx, j in enumerate(maps[i]):
        if j == 0:
            empty.append((i, idx))
        elif j == 2:
            virus.append((i, idx))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def BFS():
    queue = deque()
    tmp = 0
    for i in virus:
        queue.append(tuple(i))

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if test[ny][nx] == 0:
                test[ny][nx] = 2
                tmp += 1
                queue.append((ny, nx))
    cnt.append(tmp)


for obj in combinations(empty, 3):
    test = copy.deepcopy(maps)
    for i in obj:
        y, x = i[0], i[1]
        test[y][x] = 1
    BFS()

cnt.sort()
print(len(empty) - cnt[0] - 3)