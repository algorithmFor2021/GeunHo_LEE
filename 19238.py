# maps = n x n, 승객 : m 명
# 출발지에서만 탑승, 도착지에서만 하차
# 택시기준 가장 가까운 승객 픽업 - 여러면 이라면 행이 더 작은 사람 , 행까지 같으면 열이 더 작은 사람
# 한칸 이동할때 연료 1 소모, 도착지 도착하면 이동한 양의 2배 충전
# 이동 도중 연료 오링 - 실패 , 도착과 동시에 연료 오링 - 성공
# visted = [] 만들어서 벽 좌표들은 처음부터 False로 잡고 시작하면될듯 - 그럴필요 없을듯
from collections import deque

n, m, fuel = map(int, input().split())
maps = []
goal = deque()

for j in range(n):
    maps.append(list(map(int,input().split())))

ty, tx = map(int,input().split())
taxi = [(ty-1, tx -1)]

for j in range(m):
    sy, sx, gy, gx = map(int,input().split())
    maps[sy - 1][sx - 1] = [2, j] # type 을 기준으로 승객을 찾아주려한다.
    goal.append(((gy - 1, gx - 1)))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def findClient(fuel): # 승객 태우러 가는 BFS
    y, x = taxi.pop()
    if type(maps[y][x]) == list: # 성분이 2개짜리인걸 찾아준다.
        tmp = (0, maps[y][x][1])
        maps[y][x] = 0 # 승객(2)을 태우면 그 칸은 0으로 바꿔준다.
        taxi.append((y, x))
        return tmp # 소모 연료 , 목적지 인덱스

    visited = [[False for i in range(n)] for j in range(n)]  # 방문 확인용
    visited[y][x] = True

    cnt = 0
    queue = deque()
    queue.append((cnt, y, x))  # 택시 위치에서 시작
    tmpLst = []

    while queue:
        cnt, y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue  # 영역밖 or 이미 지나온 값 or 벽

            if visited[ny][nx] is True or maps[ny][nx] == 1:
                continue

            if type(maps[ny][nx]) == list:
                tmp = (cnt + 1, maps[ny][nx][1], ny, nx)
                tmpLst.append(tmp)
                visited[ny][nx] = True

            elif maps[ny][nx] == 0:
                queue.append((cnt + 1, ny, nx))
                visited[ny][nx] = True


    if len(tmpLst) == 0:
        return (-1,-1) # 가능한 손님이 없었던 경우
    tmpLst.sort()
    # 카운트가 가장 작은게 1개면 그걸로 리턴 , 아니라면 윗행 왼쪽열 손님을 태워주고 싶다.
    tmp1 = tmpLst[0] # 카운트가 가장 작은 값
    if tmp1[0] > fuel:
        return (-1,-1) # 가장 작은값이 연료 크기를 넘겨 버리면 불가능
    for j in range(1, len(tmpLst)):
        if tmpLst[j][0] > tmp1[0]:
            break # 더이상 tmp1(최소값)과 같은 값이 없다면 빠져나온다.
        if tmpLst[j][0] == tmp1[0]: # cnt가 같은 값이라면
            if tmpLst[j][2] < tmp1[2]:
                tmp1 = tmpLst[j] # 더 작은 행을
            elif tmpLst[j][2] == tmp1[2]: # 그마저도 같다면
                if tmpLst[j][3] < tmp1[3]:
                    tmp1 = tmpLst[j] # 더 작은 열을 선택해 주겠다.

    maps[tmp1[2]][tmp1[3]] = 0
    taxi.append((tmp1[2], tmp1[3]))
    tmp = (tmp1[0], tmp1[1])
    return tmp


def findGoal(gy,gx, fuel): # 승객 데려다 주는 BFS
    y, x = taxi.pop()
    if y == gy and x == gx:
        taxi.append((y, x))
        return 0 # 출발지와 도착지가 같은경우

    visited = [[False for i in range(n)] for j in range(n)]  # 방문 확인용
    visited[y][x] = True

    cnt = 0
    queue = deque()
    queue.append((cnt, y, x, fuel)) # 택시 위치에서 시작

    while queue:
        cnt, y, x, fuel = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue # 영역밖 or 이미 지나온 값 or 벽
            if visited[ny][nx] is True or maps[ny][nx] == 1:
                continue
            if fuel - 1 < 0:
                return -1  # cnt 값이 -1 로 리턴되면 실패임을 알림

            if gy == ny and gx == nx:
                taxi.append((ny, nx)) # 택시는 여기로 움직임
                return cnt + 1 # 이것의 2배를 fuel 에 충전해 줘야함.
            else:
                queue.append((cnt + 1, ny, nx, fuel - 1))
                visited[ny][nx] = True
    return -1 # 큐를 빠져나올동안 못찾았다면


for _ in range(m):
    tmp, goal_idx = findClient(fuel) # 같은 BFS를 써주면 안될것같음.
    if tmp == -1:
        fuel = -1
        break # 승객을 태우러 못가는 경우
    fuel -= tmp

    y, x = goal[goal_idx]
    tmp = findGoal(y, x, fuel)
    if tmp == -1:
        fuel = -1
        break # 승객을 내려주러 못가는 경우
    if tmp != None:
        fuel += tmp

print(fuel)

# print(taxi)
# print(start)
# print(maps)