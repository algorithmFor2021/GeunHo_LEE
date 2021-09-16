# maps: n x n
# 학생: 1 ~ n^2
# 4방향 인접
# 1. 비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은자리
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
from collections import deque

n = int(input())
maps = [[0 for i in range(n)] for j in range(n)]
favorite = dict()
order = deque()
for i in range(n*n):
    a, b, c, d, e = map(int, input().split())
    favorite[a] = (b, c, d, e)
    order.append(a)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def find(tmp, now):
    a, b, c, d = favorite[now]
    possible = set()
    # 1번 조건
    for j in range(n):
        for i in range(n):
            if maps[j][i] == a or maps[j][i] == b or maps[j][i] == c or maps[j][i] == d:
                for k in range(4):
                    ny = j + dy[k]
                    nx = i + dx[k]
                    if ny < 0 or nx < 0 or ny >= n or nx >= n:
                        continue
                    # 인접해 있더라도 이미 누가 앉아있으면 카운팅 x
                    if maps[ny][nx] == 0:
                        tmp[ny][nx] += 1
                        possible.add((ny, nx))
    tmp_val = 0
    res_1 = []
    for obj in possible:
        y, x = obj
        if tmp[y][x] > tmp_val:
            res_1.clear()
            res_1.append((y, x))
            tmp_val = tmp[y][x]
        elif tmp[y][x] == tmp_val:
            res_1.append((y, x))
    possible.clear()

    if len(res_1) == 1:
        y, x = res_1.pop()
        maps[y][x] = now
        return

    # 2번 조건 - '0'개 여서 넘어온 경우와 '여러개' 여서 넘어온 경우를 구분해야함
    # case 1 : 1에서 '0'개로 넘어온 경우
    elif len(res_1) == 0:
        for j in range(n):
            for i in range(n):
                if maps[j][i] == 0:
                    for k in range(4):
                        ny = j + dy[k]
                        nx = i + dx[k]
                        if ny < 0 or nx < 0 or ny >= n or nx >= n:
                            continue
                        if maps[ny][nx] == 0:
                            tmp[j][i] += 1
                            possible.add((j, i))
    # case 2 : 1에서 '여러개' 로 넘어온 경우
    elif len(res_1) > 1:
        tmp = [[0 for i in range(n)] for j in range(n)]
        for obj in res_1:
            y, x = obj
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= n or nx >= n:
                    continue
                if maps[ny][nx] == 0:
                    tmp[y][x] += 1
                    possible.add((y, x))
        # 중요 포인트
        # 이후에 possible 을 기준으로 반복문을 돌릴건데 1번에서 여러개를 받았지만
        # 2번 조건에서는 아무것도 만족하지 않을수 있다.
        # 그런경우에는 1번에서 받았던 값들을 그대로 전달 받아 사용해야 한다.
        if len(possible) == 0:
            possible = set(res_1)

    tmp_val = 0
    res_2 = []
    for obj in possible:
        y, x = obj
        if tmp[y][x] > tmp_val:
            res_2.clear()
            res_2.append((y, x))
            tmp_val = tmp[y][x]
        elif tmp[y][x] == tmp_val:
            res_2.append((y, x))
    possible.clear()
    if len(res_2) == 1:
        y, x = res_2.pop()
        maps[y][x] = now

    # 3번조건 - 마찬가지로 '0'개 여서 넘어온 경우와 '여러개' 여서 넘어온 경우를 구분해야함
    # case 1 : 2에서 '0'개로 넘어온 경우
    elif len(res_2) == 0:
        for j in range(n):
            flag = True
            for i in range(n):
                if maps[j][i] == 0:
                    maps[j][i] = now
                    flag = False
                    break
            if flag is False:
                break
    # case 2 : 2에서 '여러개' 로 넘어온 경우
    else:
        res_3 = sorted(res_2, key=lambda item: (item[0], item[1]))
        y, x = res_3[0]
        maps[y][x] = now


def satisfy():
    ans = 0
    for y in range(n):
        for x in range(n):
            cnt = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= n or nx >= n:
                    continue
                if maps[ny][nx] in favorite[maps[y][x]]:
                    cnt += 1
            if cnt != 0:
                ans += int(10 ** (cnt-1))
    return ans


while order:
    tmp = [[0 for i in range(n)] for j in range(n)]
    now = order.popleft()
    find(tmp, now)
result = satisfy()

print(result)