# DFS 방문 순서는 dfs함수에서 // x를 방문 이라고 적힌 곳에 도착한 정점 번호를 순서대로 나열한 것이다.

import sys
from collections import deque
sys.setrecursionlimit(10**5)

n = int(input())
maps = [[]for i in range(n+1)]
visited = [False for i in range(n+1)]
# 양방향 그래프
for j in range(n - 1):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)
route = deque(map(int, input().split()))
result = []
stack = []
idx = 0


def dfs(now):
    global idx
    if visited[now] is True:
        return
    visited[now] = True
    if route[idx] in stack[-1]:
        stack[-1].remove(route[idx])
        if len(stack[-1]) == 0:
            stack.pop()
        stack.append(maps[now])
        #############################################3#
        # 양방향 그래프 특성상 연결요소를 집어넣으면 무조건 부모노드까지 같이 넣어진다
        # 그걸 빼주는 작업
        for i in maps[now]:
            if visited[i] is True:
                stack[-1].remove(i)
        if len(stack[-1]) == 0:
            stack.pop()
        ###############################################33
        idx += 1
        if idx >= len(route):
            print(1)
            sys.exit(0)
        else:
            dfs(route[idx])
    else:
        print(0)
        sys.exit(0)


if route[0] == 1:
    stack.append([1])
    dfs(1)
else:
    print(0)