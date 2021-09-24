# maps : n x n
# 블록 : 검은색 = -1, 무지개 = 0, 일반블록 = 1 ~ M
# 블록 그룹(2이상) : 일반블록 적어도 하나, 무지개 블록 가능, 검정 블록 불가
# 블록 그룹의 기준 : 무지개 블록 제외 가장 작은 행 번호 -> 여러개면 가장 작은 열 번호

# 크기가 가장 큰 블록 그룹을 찾는다. 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹,
# 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
# 1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.
# 격자에 중력이 작용한다.
# 격자가 90도 반시계 방향으로 회전한다.
# 다시 격자에 중력이 작용한다.
import copy
from collections import deque

n, m = map(int, input().split())
maps = []
visited = [[False for j in range(n)]for i in range(n)]
for i in range(n):
    maps.append(list(map(int, input().split())))
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
# 라벨링 결과를 넣어줄거임 - 그 결과를 sorted 해서 점수로 반환시키는 작업을 함
standard = []


# 맵 전체를 BFS 해주면서 라벨링 진행 (크기, 무지개블록 갯수, 기준행, 기준열)
def labelling(org_y, org_x, org_val):
    queue = deque()
    queue.append((org_y, org_x))
    visited[org_y][org_x] = True
    tmp_visited = copy.deepcopy(visited)
    cnt = 1
    rainbow_cnt = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 영역 밖 or 이미 방문
            if ny < 0 or nx < 0 or ny >= n or nx >= n or tmp_visited[ny][nx] is True:
                continue
            # 일반 블록, 무지개 블록 구분해야 함
            if maps[ny][nx] == 0:
                cnt += 1
                rainbow_cnt += 1
                tmp_visited[ny][nx] = True
                queue.append((ny, nx))
                # 기준 블럭은 무지개 블럭이 아니여야함....이것때문에 계속 틀림
                # if ny <= org_y:
                #     org_y = ny
                #     if nx < org_x:
                #         org_x = nx
            elif maps[ny][nx] == org_val:
                cnt += 1
                visited[ny][nx] = True
                tmp_visited[ny][nx] = True
                queue.append((ny, nx))
    # 그룹에 속한 블록이 2개 이상인 경우만 블록 그룹이라 하기로 함
    if cnt >= 2:
        # standard 그룹 선정 -> 해당 그룹은 다시 BFS 로 찾아야 하는지?(비효율적여보임)
        standard.append((cnt, rainbow_cnt, org_y, org_x, org_val))


def scoring(org_y, org_x, org_val):
    queue = deque()
    queue.append((org_y, org_x))
    maps[org_y][org_x] = -2
    visited[org_y][org_x] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n or visited[ny][nx] is True:
                continue
            if maps[ny][nx] == 0 or maps[ny][nx] == org_val:
                visited[ny][nx] = True
                # 제거된 칸은 -2로 표현하겠다.
                maps[ny][nx] = -2
                queue.append((ny, nx))


def gravity():
    # 맵 전체를 돌면서
    for i in range(n):
        for j in range(n-1, -1, -1):
            # 블럭이 발견되면
            if maps[j][i] >= 0:
                new_j = j
                # 아래칸들을 확인한다.
                for k in range(n):
                    new_j += 1
                    # 영역 밖
                    if new_j >= n:
                        break
                    # 빈칸인 경우 스위칭
                    if maps[new_j][i] == -2:
                        maps[new_j - 1][i], maps[new_j][i] = maps[new_j][i], maps[new_j - 1][i]
                    # 빈칸이 없으면 탈출
                    else:
                        break


def rotate():
    tmp = copy.deepcopy(maps)
    for j in range(n):
        for i in range(n):
            maps[j][i] = tmp[i][n-1-j]


score = 0
while True:
    for j in range(n):
        for i in range(n):
            if maps[j][i] > 0 and visited[j][i] is False:
                labelling(j, i, maps[j][i])
    # 라벨링을 했는데 그룹이 생기지 않는경우 탈출
    if len(standard) == 0:
        break
    # 블록 크기, 무지개 블록갯수, 기준행, 기준열을 통한 정렬
    standard = sorted(standard, key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    cnt, rainbow_cnt, org_y, org_x, org_val = standard[0]
    score += (cnt**2)
    visited = [[False for j in range(n)] for i in range(n)]
    scoring(org_y, org_x, org_val)
    gravity()
    rotate()
    gravity()
    standard.clear()
    visited = [[False for j in range(n)] for i in range(n)]

print(score)

# 6 3
# 1 1 1 0 0 0
# 1 1 1 0 0 0
# 1 1 3 0 0 0
# 0 0 0 2 2 2
# 0 0 0 2 2 2
# 0 0 0 2 2 2