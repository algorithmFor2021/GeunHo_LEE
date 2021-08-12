# maps = n x m
# (1, 1) -> (n, m), 이동하는 최단경로 찾기
# 0 : 이동가능 , 1 : 벽
# k 개까지 벽 부수기 가능, 불가능 할때는 -1 출력
import copy
from collections import deque

n, m = map(int, input().split())
maps = []
# 부셔져서 도착한곳 : 0, 안부시고 도착한곳 : 1
visit = [[[False for i in range(m)]for j in range(n)]for k in range(2)]
for j in range(n):
    tmp = list(map(int, input().strip()))
    maps.append(tmp)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(route, visited):
    queue = deque()
    # y, x, cnt, 벽 부셨는지 여부
    queue.append((0, 0, 1, False))
    visited[0][0][0] = True
    visited[1][0][0] = True
    while queue:
        y, x, cnt, crash = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 영역 밖, 이미 방문한 경우
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            # 목표점에 도착한 경우
            if ny == (n - 1) and nx == (m - 1):
                return cnt + 1
            # 벽인 경우
            if route[ny][nx] == 1:
                # 벽이 부셔진 적이 없고 부실수 있다면
                if visited[1][ny][nx] is False and crash is False:
                    queue.append((ny, nx, cnt + 1, True))
                    visited[1][ny][nx] = True
            # 길인 경우
            else:
                # 부수고 도착한 경우
                if crash is True:
                    if visited[1][ny][nx] is False:
                        queue.append((ny, nx, cnt + 1, crash))
                        visited[1][ny][nx] = True
                # 그냥 도착한 경우
                else:
                    if visited[0][ny][nx] is False:
                        queue.append((ny, nx, cnt + 1, crash))
                        visited[0][ny][nx] = True
    return -1


if n == 1 and m == 1:
    print(1)
else:
    result = bfs(maps, visit)
    print(result)