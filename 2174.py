# maps = A x B
# 로봇 : n 개 , 명령 : m 번 -> 명령은 순차적으로 실행
# L: 로봇이 향하고 있는 방향을 기준으로 왼쪽으로 90도 회전한다.
# R: 로봇이 향하고 있는 방향을 기준으로 오른쪽으로 90도 회전한다.
# F: 로봇이 향하고 있는 방향을 기준으로 앞으로 한 칸 움직인다.
from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())
maps = [[0 for i in range(a)]for j in range(b)]
robots = [0 for i in range(n+1)]
flag = True
# E 기준으로 R 방향으로 pole 리스트 선언
pole = ['E', 'S', 'W', 'N']
result = "OK"
operator = deque()

for i in range(n):
    x, y, dir = map(str, input().split())
    x = int(x) - 1
    y = b - int(y)
    if dir == 'E':
        dir = 0
    elif dir == 'S':
        dir = 1
    elif dir == 'W':
        dir = 2
    elif dir == 'N':
        dir = 3
    maps[y][x] = i+1
    robots[i+1] = [y, x, dir]
for i in range(m):
    operator.append(list(map(str, input().split())))


def move(idx, num):
    global flag
    global result
    y, x, dir = robots[idx]
    maps[y][x] = 0
    result = "OK"
    for i in range(num):
        if pole[dir] == 'E':
            x += 1
        elif pole[dir] == 'W':
            x -= 1
        elif pole[dir] == 'S':
            y += 1
        elif pole[dir] == 'N':
            y -= 1
        # 탈출 조건
        if x < 0 or y < 0 or x >= a or y >= b:
            result = "Robot X crashes into the wall".replace('X', str(idx))
            flag = False
            break
        if maps[y][x] != 0:
            result = "Robot X crashes into robot Y".replace('X', str(idx))
            result = result.replace('Y', str(maps[y][x]))
            flag = False
            break

    if flag is not False:
        maps[y][x] = idx
        robots[idx] = [y, x, dir]
    return result


while operator:
    oper = operator.popleft()
    # 로봇, 명령, 반복횟수
    oper_robot, oper_order, oper_num = int(oper[0]), oper[1], int(oper[2])
    # 이동하는 경우
    if oper_order == 'F':
        result = move(oper_robot, oper_num)
    # 방향을 바꾸는 경우
    elif oper_order == 'L':
        org_dir = robots[oper_robot][2]
        fix_dir = org_dir - oper_num
        fix_dir %= 4
        robots[oper_robot][2] = fix_dir
    elif oper_order == 'R':
        org_dir = robots[oper_robot][2]
        fix_dir = org_dir + oper_num
        fix_dir %= 4
        robots[oper_robot][2] = fix_dir

    if result != "OK":
        print(result)
        exit(0)
print(result)