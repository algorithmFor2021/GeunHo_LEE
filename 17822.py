# n 개의 원판
# 각 원판에는 m 개의 숫자가 적혀있음
# deque 의 rotate 를 이용하면 더 쉽게 구현할수도 있다.

from collections import deque

n, m, t = map(int, input().split())
circles = []
for i in range(n):
    circles.append(list(map(int, input().split())))
operator = deque()
for i in range(t):
    operator.append(list(map(int, input().split())))


def rotate_forward(circle):
    return circle[m-1:] + circle[:m-1]


def rotate_backward(circle):
    return circle[1:] + circle[:1]


result = 0
while operator:
    x, d, k = operator.popleft()
    forDel = []
    # x 의 배수 회전판만 선택
    for i in range(x-1, n, x):
        # 시계방향 k칸 회전
        if d == 0:
            for _ in range(k):
                circles[i] = rotate_forward(circles[i])
        # 반시계방향 k칸 회전
        else:
            for _ in range(k):
                circles[i] = rotate_backward(circles[i])

    # 인접한 숫자 찾는 부분
    for j in range(n):
        for i in range(m):
            if circles[j][i] == 0:
                continue
            if circles[j][i-1] == circles[j][i]:
                forDel.append((j, i))
                forDel.append((j, i-1))
            if j != n-1 and circles[j][i] == circles[j+1][i]:
                forDel.append((j, i))
                forDel.append((j+1, i))

    # 인접한 숫자가 있는 경우
    if len(forDel) != 0:
        while forDel:
            j, i = forDel.pop()
            circles[j][i] = 0
    # 없는 경우
    else:
        cnt = 0
        tmp = []
        tmpSum = 0
        for j in range(n):
            for i in range(m):
                if circles[j][i] != 0:
                    cnt += 1
                    tmpSum += circles[j][i]
                    tmp.append((j, i, circles[j][i]))
        if cnt != 0:
            avg = tmpSum / cnt
            while tmp:
                j, i, val = tmp.pop()
                if val > avg:
                    circles[j][i] -= 1
                elif val < avg:
                    circles[j][i] += 1

for j in range(n):
    result += sum(circles[j])

print(result)