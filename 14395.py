import copy
from collections import deque

s, t = map(int, input().split())
operator = ['*', '+', '-', '/']
result = [[] for i in range(4)]
visited = []


def bfs(start, target):
    queue = deque()
    queue.append([start])
    visited.append(start)
    while queue:
        pre_now = queue.popleft()
        now = pre_now.pop()
        for i in range(4):
            tmp_now = copy.deepcopy(pre_now)
            tmp_now.append(i)

            if i == 0:
                tmp = now * now
                if tmp > 10 ** 9:
                    continue
            elif i == 1:
                tmp = now + now
                if tmp > 10 ** 9:
                    continue
            elif i == 2:
                tmp = now - now
            elif i == 3 and now != 0:
                tmp = now // now

            if tmp == target:
                return tmp_now
            if tmp in visited:
                continue
            visited.append(tmp)
            tmp_now.append(tmp)
            queue.append(tmp_now)

    return -1


real_ans = ''
if s is t:
    print(0)
else:
    ans = bfs(s, t)
    if ans == -1:
        print(-1)
    else:
        for i in ans:
            real_ans += operator[i]
        print(real_ans)
