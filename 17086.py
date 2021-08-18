# 2 <= n,m <= 50
# 맵 전체를 확인하며 각 칸마다 최소 거리 입력 - BFS
# 최소거리 맵 전체를 확인하여 그중 최대값 출력
# 위의 기능을 하는 함수를 각각 한개씩 만들어서 사용하면 될 듯
# 빈칸 : 0, 상어 : -2, 지나간 길 : -1
import copy
from collections import deque

n, m = map(int, input().split())
maps = []
# 방문 확인용
visited = [[0 for i in range(m)] for j in range(n)]
for j in range(n):
    tmp = list(map(int, input().split()))
    maps.append(tmp)
    for idx, i in enumerate(tmp):
        if i == 1:
            # 상어가 있는 칸은 음수의 초기값을 준다. - 마지막 최대 값 계산에서 제외되게 하기위해서
            maps[j][idx] = -2

# 8방향 탐색
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]


def BFS(sy, sx):
    cnt = 0
    tmp_visited = copy.deepcopy(visited)
    tmp_visited[sy][sx] = -1
    queue = deque()
    queue.append((sy, sx, cnt))
    while queue:
        y, x, cnt = queue.popleft()
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            # 맵을 벗어나는 경우 - 상어와 거리가 최대인 곳을 찾는것이므로, 상어를 만나지 않는 방향은 고려해 줄 필요X, 이미 방문한 길인 경우
            if ny < 0 or nx < 0 or ny >= n or nx >= m or tmp_visited[ny][nx] == -1:
                continue
            if maps[ny][nx] == -2:
                maps[sy][sx] = cnt + 1
                return maps[sy][sx]
            else:
                queue.append((ny, nx, cnt + 1))
                tmp_visited[ny][nx] = -1
    return maps[sy][sx]


result = 0
for j in range(n):
    for i in range(m):
        if maps[j][i] == 0:
            k = BFS(j, i)
            if k > result:
                result = k
print(result)