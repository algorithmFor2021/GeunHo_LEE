# 대기실 : 5개
# 각 대기실 크기 : 5x5
# 응시자들끼리 맨해튼 거리가 2 이하로 앉으면 안됨 but 사이를 전부 파티션이 막고있으면 가능
# 응시자 : P, 빈 테이블 : O, 파티션 : X
# dy, dx를 이용해서 P 기준으로 총 12케이스를 확인하면 됨
from collections import deque

answer = []
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
dy2 = [-2, 2, 0 ,0]
dx2 = [0, 0, -2, 2]
dy_diagonal = [-1, 1, -1, 1]
dx_diagonal = [-1, -1, 1, 1]


def bfs(maps, group_p):
    while group_p:
        y, x = group_p.popleft()
        # 거리가 1인 경우 (무조건 return 0)
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny >= 5 or nx >= 5:
                continue
            if maps[ny][nx] == 'P':
                return 0
        # 거리가 2인경우 (바로 앞이 'X' 인지 확인)
        for i in range(4):
            ny, nx = y + dy2[i], x + dx2[i]
            if ny < 0 or nx < 0 or ny >= 5 or nx >= 5:
                continue
            # 거리가 2인곳에 사람이 있고 그 바로앞에 벽이 없다면
            if maps[ny][nx] == 'P' and maps[y + dy[i]][x + dx[i]] != 'X':
                return 0
        # 대각선인 경우
        for i in range(4):
            ny, nx = y + dy_diagonal[i], x + dx_diagonal[i]
            if ny < 0 or nx < 0 or ny >= 5 or nx >= 5:
                continue
            if maps[ny][nx] == 'P':
                if i == 0:
                    if maps[y-1][x] != 'X' or maps[y][x-1] != 'X':
                        return 0
                elif i == 1:
                    if maps[y+1][x] != 'X' or maps[y][x-1] != 'X':
                        return 0
                elif i == 2:
                    if maps[y-1][x] != 'X' or maps[y][x+1] != 'X':
                        return 0
                elif i == 3:
                    if maps[y+1][x] != 'X' or maps[y][x+1] != 'X':
                        return 0
    return 1


for i in range(5):
    maps = []
    group_p = deque()
    for jdx, obj in enumerate(places[i]):
        tmp = list(map(str, obj.strip()))
        maps.append(tmp)
        for idx, j in enumerate(tmp):
            if j == 'P':
                group_p.append((jdx, idx))
    tmp = bfs(maps, group_p)
    answer.append(tmp)
    print(maps)
    print(group_p)

print(answer)