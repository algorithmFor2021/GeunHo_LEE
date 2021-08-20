# 백트래킹 - 유망한지 결정하는 함수
# + 특별히 조건에 반하지 않으면 계속해서 진행해 나갈 함수 -> 2개 함수를 기본적으로 구현해야 한다.
# DFS 실패시 초기화 해주는 조건의 필요성

import sys

maps = []
zeros = []

for j in range(9):
    tmp = list(map(int, input().split()))
    maps.append(tmp)
    for idx, i in enumerate(tmp):
        if i == 0:
            zeros.append((j, idx))


# 유망한지 결정 -> 행, 열, 3 * 3 체크
def checking(y, x):
    lst = [i+1 for i in range(9)]
    sy = y // 3
    sx = x // 3
    # 같은 행 비교
    for i in range(9):
        if maps[y][i] in lst:
            lst.remove(maps[y][i])
    # 같은 열 비교
    for j in range(9):
        if maps[j][x] in lst:
            lst.remove(maps[j][x])
    # 3 * 3 비교
    ny = 3 * sy
    nx = 3 * sx
    for j in range(ny, ny + 3):
        for i in range(nx, nx + 3):
            if maps[j][i] in lst:
                lst.remove(maps[j][i])
    return lst


def dfs(now):
    if now == len(zeros):
        for i in range(9):
            print(' '.join(map(str, maps[i])))
        sys.exit(0)
    y, x = zeros[now]
    promissing = checking(y, x)
    for obj in promissing:
        maps[y][x] = obj
        dfs(now + 1)
        # dfs 가 실패한 경우 원래대로 돌아와야 함 -> 왜? 어차피 실패하면 반복문의 다음 값이 들어갈텐데?
        # 이 하나의 값만 보면 맞는 생각이지만 dfs 특성상 실패하기 직전까지의 깊이에 있는 모든 인자에 값들이 들어가 있을거임
        maps[y][x] = 0
    else:
        return

dfs(0)