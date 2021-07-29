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

n, m, k = map(int, input().split())
tree = [[[]for i in range(n)]for j in range(n)]
maps = [[5 for i in range(n)]for j in range(n)]
feed = []
# 가을 : 8방향 연산용
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
for i in range(n):
    feed.append(list(map(int, input().split())))
for i in range(m):
    r, c, age = map(int, input().split())
    # age 로 구성된 2차원 배열을 만든다
    tree[r-1][c-1].append(age)


# 봄 + 여름
def spring():
    for j in range(n):
        for i in range(n):
            if tree[j][i]:
                tmp = []
                die = 0
                tree[j][i].sort()
                for z in range(len(tree[j][i])):
                    if maps[j][i] >= tree[j][i][z]:
                        maps[j][i] -= tree[j][i][z]
                        tmp.append(tree[j][i][z] + 1)
                    else:
                        die += (tree[j][i][z] // 2)
                maps[j][i] += die
                tree[j][i] = []
                tree[j][i] += tmp


def fall():
    for y in range(n):
        for x in range(n):
            if tree[y][x]:
                for z in range(len(tree[y][x])):
                    if tree[y][x][z] % 5 == 0:
                        for i in range(8):
                            ny = y + dy[i]
                            nx = x + dx[i]
                            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                                continue
                            tree[ny][nx].append(1)


for i in range(k):
    spring()
    fall()
    # 겨울 : 2차원 배열의 합
    maps = [[maps[jj][ii] + feed[jj][ii] for ii in range(n)]for jj in range(n)]

result = 0
for j in range(n):
    for i in range(n):
        result += len(tree[j][i])

print(result)