# maps : n x n
# 마지막행과 첫번째 행은 연결, 마지막열과 첫번째 열은 연결 - maps 는 무한히 연결되어있다고 생각
# m 번 명령이 들어옴
# 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생김
# 모든 구름이 d 방향 s 칸 이동
# 구름이 있는 칸의 물의 양 1 증가
# 이번에 증가한 칸에서 물복사 버그 실행
# 대각선으로 거리가 1인칸중 0이 아닌 칸 수만큼 +1 - 이때는 maps 벗어나는 범위는 체크x
# 마지막으로 maps 를 탐색하며 값이 2 이상인 칸은 -2 해주고 구름이 생긴다 - 3에서 사라진 칸은 여기서 제외된다.

from collections import deque


n, m = map(int, input().split())
maps = []
operator = deque()
for i in range(n):
    maps.append(list(map(int, input().split())))
for i in range(m):
    operator.append(list(map(int, input().split())))
# 8 방향 움직임 - 인덱스에 맞춰 구현
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
default_cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
# 이번 턴에 구름이 생겨 물이 증가한 칸 -> 물복사 대상 리스트
cloud = []
rest_cloud = deque()
flag = False


def make_cloud(d, s):
    if flag is False:
        for i in range(4):
            ny = default_cloud[i][0] + s * dy[d]
            nx = default_cloud[i][1] + s * dx[d]
            while ny >= n:
                ny -= n
            while nx >= n:
                nx -= n
            while ny < 0:
                ny += n
            while nx < 0:
                nx += n
            maps[ny][nx] += 1
            cloud.append((ny, nx))
    else:
        while rest_cloud:
            y, x = rest_cloud.popleft()
            ny = y + s * dy[d]
            nx = x + s * dx[d]
            while ny >= n:
                ny -= n
            while nx >= n:
                nx -= n
            while ny < 0:
                ny += n
            while nx < 0:
                nx += n
            maps[ny][nx] += 1
            cloud.append((ny, nx))


def water_copy():
    for obj in cloud:
        cnt = 0
        y, x = obj[0], obj[1]
        for i in range(2, 9, 2):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if maps[ny][nx] > 0:
                cnt += 1
        maps[y][x] += cnt


def make_rest_cloud():
    for j in range(n):
        for i in range(n):
            if maps[j][i] >= 2 and (j, i) not in cloud:
                rest_cloud.append((j, i))
                maps[j][i] -= 2


while operator:
    d, s = operator.popleft()
    make_cloud(d, s)
    flag = True
    water_copy()
    make_rest_cloud()
    cloud.clear()
result = 0
for j in range(n):
    for i in range(n):
        if maps[j][i] != 0:
            result += maps[j][i]
print(result)