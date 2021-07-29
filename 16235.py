# maps : n x n
# 각 칸 : (r, c) - (1, 1) 부터 시작
# 시작시 모든 칸의 양분 : 5
# m 개의 나무를 구매
# 봄 : 나무가 자신의 나이만큼 양분 흡수, 나이 1증가 - 땅에 있는 양분까지만 흡수 가능
# 하나의 칸에 여러개의 나무가 있으면 어린 나무부터 양분 흡수
# 자신의 나이만큼 양분을 못 먹은 나무는 즉사
# 여름 : 즉사한 나무의 나이 / 2 만큼 그 칸의 양분으로 변한다
# 가을 : 나무의 나이가 5의 배수인경우 인접한 8칸으로 나이가 1인 나무 생성
# 겨울 : 각 칸 마다 주어진 입력대로 양분 추가
# k 년이 지난 후 살아 있는 나무의 개수 출력
from collections import deque
n, m, k = map(int, input().split())
tree = []
# 나이만큼 못먹은 경우 die 리스트에 넣어놨다가 계절이 바뀔때 한번에 처리
die = []
maps = [[5 for i in range(n)]for j in range(n)]
feed = []
# 가을 : 8방향 연산용
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
for i in range(n):
    feed.append(list(map(int, input().split())))
for i in range(m):
    y, x, age = map(int, input().split())
    tree.append((y-1, x-1, age))
tree = deque(sorted(tree, key=lambda item: (item[2])))
def spring(tree):
    for i in range(len(tree)):
        y, x, age = tree.popleft()
        # 양분이 충분하면 나이만큼 빨아먹고
        if maps[y][x] >= age:
            maps[y][x] -= age
            tree.append((y, x, age + 1))
        # 그렇지 못하면 die 리스트에 추가해놓는다.
        else:
            die.append((y, x, age))
    return tree
def fall(tree):
    tmp = deque()
    for j in range(len(tree)):
        if tree[j][2] % 5 == 0:
            y, x = tree[j][0], tree[j][1]
            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= n or nx >= n:
                    continue
                tmp.append((ny, nx, 1))
    return tmp + tree
for i in range(k):
    tree = spring(tree)
    # 여름
    while die:
        y, x, age = die.pop()
        maps[y][x] += (age // 2)
    tree = fall(tree)
    # 겨울 : 2차원 배열의 합
    maps = [[maps[jj][ii] + feed[jj][ii] for ii in range(n)]for jj in range(n)]
print(len(tree))
# 43% 시간초과 - 이유