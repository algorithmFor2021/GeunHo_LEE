# 맵을 어떻게 구성할지 - 알파벳 별 구분을 할건지?
# 모든 요소에 대해 bfs?
# 한 요소에 대해 bfs 진행 후 사이클이 안만들어 졌다면 visted_org에서 False 처리
# 키포인트는 bfs 후 다시 첫점에서 만나는가? 가 아니라 bfs 를 하는 요소들끼리 만나는가? 를 판단하는 것

import copy
from collections import deque

n, m = map(int, input().split())
maps = []
# bfs 진행 할때마다 새로 만들어 줘야 함
visited_org = [[False for i in range(m)]for j in range(n)]
for i in range(n):
    maps.append(list(map(str, input().strip())))
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(sy, sx):
    visited = copy.deepcopy(visited_org)
    queue = deque()
    queue.append((sy, sx))
    visited[sy][sx] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny, nx) in queue:
                return "Yes"
            # 영역을 벗어나는 경우, 이미 방문한 곳을 다시 방문하려는 경우
            if ny < 0 or nx < 0 or ny >= n or nx >= m or visited[ny][nx] is True:
                continue
            # 이전 요소와 다른 값인 경우
            if maps[ny][nx] == maps[sy][sx]:
                queue.append((ny, nx))
                visited[ny][nx] = True
    return "No"


for j in range(n):
    for i in range(m):
        ans = bfs(j, i)
        if ans == "Yes":
            print(ans)
            exit(0)
        visited_org[j][i] = True
print(ans)