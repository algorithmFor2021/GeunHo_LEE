# maps = r x c (0, 0)부터 시작
# 낚시왕 : (0, 0) 시작 ->(0, c) 도착시 종료
# 상어 : (1, 1) ~ (r, c) 까지 분포, 크기, 속도
# 낚시왕 : 오른쪽으로 한칸 이동(0, +1), 땅과 가장 가까운 상어 잡음(맵에서 상어 사라짐), 상어 이동
# 상어 : 입력으로 주어진 속도/방향으로 이동, 맵 밖으로 넘어가면 방향 바꿔서 이동
# 상어가 이동하다 보면 한칸에 여러마리 있을 수 있음 -> 가장 큰 상어 제외하고 전부 삭제(잡아 먹힘)
import copy
r, c, m = map(int, input().split())
maps = [[0 for i in range(c + 1)] for j in range(r + 1)]
# 움직인 상어 넣는 용도
oper = [[0 for i in range(c + 1)] for j in range(r + 1)]
for i in range(m):
    y, x, s, d, z = map(int, input().split())
    maps[y][x] = (s, d, z)
# 위, 아래, 오른쪽, 왼쪽
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]


def jaws_move():
    pool = copy.deepcopy(oper)
    for j in range(1, r+1):
        for i in range(1, c+1):
            if maps[j][i] != 0:
                y, x, s, d, z = j, i, maps[j][i][0], maps[j][i][1], maps[j][i][2]
                org_s = s
                while s > 0:
                    y += dy[d]
                    x += dx[d]
                    # 영역 벗어난 경우 움직이지말고 방향 바꿔주기
                    if y <= 0 or x <= 0 or y > r or x > c:
                        y -= dy[d]
                        x -= dx[d]
                        if d == 1:
                            d = 2
                        elif d == 2:
                            d = 1
                        elif d == 3:
                            d = 4
                        elif d == 4:
                            d = 3
                    # 영역 안에서 s 가 0이 될때까지 움직여준다.
                    else:
                        s -= 1
                # 빈 칸이거나 이미 들어온 값보다 큰 값이 들어온다면 새 값을 넣어줌
                if pool[y][x] == 0:
                    pool[y][x] = (org_s, d, z)
                elif pool[y][x][2] < z:
                    pool[y][x] = (org_s, d, z)

    return pool


result = []
for i in range(c):
    for j in range(1, r+1):
        # i + 1 열의 모든 행을 검색
        if maps[j][i+1] != 0:
            # 가장 먼저 발견되는 상어만 잡고 탈출
            result.append(maps[j][i + 1][2])
            maps[j][i+1] = 0
            break
    maps = jaws_move()
print(sum(result))