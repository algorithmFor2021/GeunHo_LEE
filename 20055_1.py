import sys

n, k = map(int,sys.stdin.readline().split())
conv = list(map(int,sys.stdin.readline().split()))
cnt = 0
cycle = 0
robot = [0] * n

while True:
    cycle += 1
    tmp1 = conv.pop(-1)
    conv.insert(0, tmp1)

    for i in range(n-2, -1, -1):
        if robot[i] == 1:
            robot[i+1] = 1
            robot[i] = 0
    if robot[n-1] == 1:
        robot[n-1] = 0

    for i in range(n-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and conv[i+1] > 0:
            robot[i+1] = 1
            robot[i] = 0
            conv[i+1] -= 1
            if conv[i+1] == 0:
                cnt += 1
    if robot[n-1] == 1:
        robot[n-1] = 0

    if robot[0] == 0 and conv[0] > 0:
        robot[0] = 1
        conv[0] -= 1
        if conv[0] == 0:
            cnt += 1

    if cnt >= k:
        break

print(cycle)