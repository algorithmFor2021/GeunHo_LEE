# 정점의 개수 : N
# 1 ~ N 정점의 양방향 그래프
# 시작 정점 : 1
from collections import deque

n = int(input())
maps = [[] for i in range(n + 1)]
visited = [False for i in range(n + 1)]
for i in range(n-1):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)
road = deque(map(int, input().split()))


def bfs(road):
    start = road[0]
    queue = deque()
    queue.append(([start], 1))
    visited[start] = True
    tmp = []
    cnt = 0
    idx = 0
    for i in range(len(road)):
        x = road[i]
        if queue[idx][1] == cnt:
            idx += 1
            cnt = 0
        if x in queue[idx][0]:
            for j in maps[x]:
                if visited[j] is True:
                    continue
                tmp.append(j)
                visited[j] = True
            if len(tmp) != 0:
                queue.append((tmp, len(tmp)))
                tmp = []
            cnt += 1
        else:
            return 0
    return 1


if road[0] != 1:
    print(0)
else:
    result = bfs(road)
    print(result)

# 5
# 1 2
# 2 3
# 1 4
# 4 5
# 1 2 4 5 3