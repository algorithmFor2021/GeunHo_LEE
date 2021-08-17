import sys
from collections import deque
from timeit import default_timer as timer
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[False for i in range(m)]for j in range(n)]
maps = []
walls = []
for j in range(n):
    tmp = list(map(int, input().strip()))
    maps.append(tmp)
    # 벽들 좌표 리스트, 벽 : -1 처리
    for idx, i in enumerate(tmp):
        if i == 1:
            walls.append((j, idx))
            maps[j][idx] = -1
final_map = [[0 for i in range(m)]for j in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def changeMap(changing, val, idx):
    for obj in changing:
        y, x = obj[0], obj[1]
        maps[y][x] = (idx, val)


def bfs(sy, sx, idx):
    queue = deque()
    queue.append((sy, sx))
    visited[sy][sx] = True
    cnt = 1
    changing = []
    changing.append((sy, sx))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            # 영역밖 or 이미 지나온 경우
            if ny < 0 or nx < 0 or ny >= n or nx >= m or visited[ny][nx] is True:
                continue
            if maps[ny][nx] == 0:
                changing.append((ny, nx))
                queue.append((ny, nx))
                visited[ny][nx] = True
                cnt += 1
    changeMap(changing, cnt, idx)


def makeMap(sy, sx):
    visited_idx = deque()
    final_map[sy][sx] = 1
    for i in range(4):
        ny, nx = sy + dy[i], sx + dx[i]
        # 영역 밖 or 벽
        if ny < 0 or nx < 0 or ny >= n or nx >= m or maps[ny][nx] == -1:
            continue
        if maps[ny][nx][0] not in visited_idx:
            final_map[sy][sx] += maps[ny][nx][1]
            visited_idx.append(maps[ny][nx][0])
    final_map[sy][sx] %= 10


# start = timer()
idx = 0
for j in range(n):
    for i in range(m):
        idx += 1
        if maps[j][i] == 0:
            bfs(j, i, idx)

for obj in walls:
    makeMap(obj[0], obj[1])

for i in range(n):
    print(''.join(map(str, final_map[i])))

# 시간초과 나는 출력 -> 출력때문에 시간초과 처음ㅎ...
# 입력뿐 아니라 출력도 고려해줘야한다.
# result = ""
# for j in range(n):
#     for i in range(m):
#         result += str(final_map[j][i])
#     if j != n-1:
#         result += "\n"
# print(timer() - start)