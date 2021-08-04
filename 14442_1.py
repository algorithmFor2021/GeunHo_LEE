import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
maps = []
visit = [[[0 for i in range(m)]for j in range(n)]for z in range(k + 1)]
for j in range(n):
    tmp = list(map(int, sys.stdin.readline().strip()))
    maps.append(tmp)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(route, cost, chance):
    queue = deque()
    # y, x, cnt, 벽 부실 기회
    queue.append((0, 0, chance))
    # cost 맵을 만들어서 더 작은값을 남기는 방식으로 진행
    for i in range(chance + 1):
        cost[i][0][0] = 1
    while queue:
        y, x, crash = queue.popleft()
        # 목표점에 도착한 경우
        if y == (n - 1) and x == (m - 1):
            return cost[crash][y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 영역 밖, 이미 방문한 경우 (먼저 방문한게 무조건 더 작은 값)
            if ny < 0 or nx < 0 or ny >= n or nx >= m or cost[crash][ny][nx] != 0:
                continue
            # 길인 경우
            if route[ny][nx] == 0:
                cost[crash][ny][nx] = cost[crash][y][x] + 1
                queue.append((ny, nx, crash))
            # 벽인 경우 - 부술 기회가 남아있고 아직 아무도 다녀가지 않은 길이어야 한다.
            # 누군가 이미 다녀 갔다면 그 값이 더 작은 값일 것이므로 진행x
            elif crash > 0 and cost[crash - 1][ny][nx] == 0:
                cost[crash - 1][y][x] = cost[crash][y][x]
                cost[crash - 1][ny][nx] = cost[crash][y][x] + 1
                queue.append((ny, nx, crash - 1))

    return -1


result = bfs(maps, visit, k)
print(result)