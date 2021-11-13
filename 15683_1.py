from collections import deque
import copy
import sys

n, m = map(int, input().split())
total = n * m
maps = [] # 전체 지도
cctv = [] # cctv 위치 , 종류
result = sys.maxsize
# 위, 아래, 오른쪽, 왼쪽
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

directions = {1: [[0], [1], [2], [3]],
              2: [[0, 1], [2, 3]],
              3: [[0, 2], [0, 3], [1, 2], [1, 3]],
              4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
              5: [[0, 1, 2, 3]]}

for j in range(n):
    tmp = list(map(int, input().split()))
    maps.append(tmp)
    for idx, i in enumerate(tmp):
        if i != 0 and i != 6:
            cctv.append((j, idx, i))
            total -= 1
        elif i == 6:
            total -= 1


def fill(y, x, arr, dir):
    cnt = 0
    init_y, init_x = y, x
    for i in dir:
        queue = deque()
        queue.append((init_y, init_x))
        while queue:
            y, x = queue.popleft()
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m or maps[ny][nx] == 6:
                break
            if arr[ny][nx] == 0:
                arr[ny][nx] = -1
                queue.append((ny, nx))
            else:
                queue.append((ny, nx))


def dfs(arr, cnt):
    global result
    if cnt == len(cctv):
        num = 0
        for j in range(n):
            num += arr[j].count(0)
        result = min(result, num)
        return
    y, x, obj_cctv = cctv[cnt]
    tmp = copy.deepcopy(arr)
    for i in directions[obj_cctv]:
        fill(y, x, tmp, i)
        dfs(tmp, cnt + 1)
        tmp = copy.deepcopy(arr)#dfs로 카운팅 해주기 직전의 fill 이전 값


dfs(maps, 0)
print(result)