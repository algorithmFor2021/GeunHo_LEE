# 윗 면은 흰색, 아랫 면은 노란색, 앞 면은 빨간색, 뒷 면은 오렌지색, 왼쪽 면은 초록색, 오른쪽 면은 파란색
# U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면

tc = int(input())


def inner_rotate(kind, rotate_dir):
    if rotate_dir == '+':
        kind[0][0], kind[0][1], kind[0][2], kind[1][2], kind[2][2], kind[2][1], kind[2][0], kind[1][0] = \
            kind[2][0], kind[1][0], kind[0][0], kind[0][1], kind[0][2], kind[1][2], kind[2][2], kind[2][1]
    else:
        kind[0][0], kind[0][1], kind[0][2], kind[1][2], kind[2][2], kind[2][1], kind[2][0], kind[1][0] = \
            kind[0][2], kind[1][2], kind[2][2], kind[2][1], kind[2][0], kind[1][0], kind[0][0], kind[0][1]


def rotate(dir, rotate_dir):
    global u, d, f, b, l, r

    if dir == 'U':
        if rotate_dir == '+':
            inner_rotate(u, rotate_dir)
            l[0], f[0], r[0], b[0] = f[0], r[0], b[0], l[0]
        else:
            inner_rotate(u, rotate_dir)
            l[0], f[0], r[0], b[0] = b[0], l[0], f[0], r[0]
    elif dir == 'D':
        if rotate_dir == '+':
            inner_rotate(d, rotate_dir)
            l[2], f[2], r[2], b[2] = b[2], l[2], f[2], r[2]
        else:
            inner_rotate(d, rotate_dir)
            l[2], f[2], r[2], b[2] = f[2], r[2], b[2], l[2]
    elif dir == 'L':
        if rotate_dir == '+':
            inner_rotate(l, rotate_dir)
            u[0][0], u[1][0], u[2][0], f[0][0], f[1][0], f[2][0], d[0][0], d[1][0], d[2][0], b[0][2], b[1][2], b[2][2] = \
                b[2][2], b[1][2], b[0][2], u[0][0], u[1][0], u[2][0], f[0][0], f[1][0], f[2][0], d[2][0], d[1][0], d[0][0]
        else:
            inner_rotate(l, rotate_dir)
            u[0][0], u[1][0], u[2][0], f[0][0], f[1][0], f[2][0], d[0][0], d[1][0], d[2][0], b[0][2], b[1][2], b[2][2] = \
                f[0][0], f[1][0], f[2][0], d[0][0], d[1][0], d[2][0], b[2][2], b[1][2], b[0][2], u[2][0], u[1][0], u[0][0]
    elif dir == 'R':
        if rotate_dir == '+':
            inner_rotate(r, rotate_dir)
            u[0][2], u[1][2], u[2][2], f[0][2], f[1][2], f[2][2], d[0][2], d[1][2], d[2][2], b[0][0], b[1][0], b[2][0] = \
                f[0][2], f[1][2], f[2][2], d[0][2], d[1][2], d[2][2], b[2][0], b[1][0], b[0][0], u[2][2], u[1][2], u[0][2]
        else:
            inner_rotate(r, rotate_dir)
            u[0][2], u[1][2], u[2][2], f[0][2], f[1][2], f[2][2], d[0][2], d[1][2], d[2][2], b[0][0], b[1][0], b[2][0] = \
                b[2][0], b[1][0], b[0][0], u[0][2], u[1][2], u[2][2], f[0][2], f[1][2], f[2][2], d[2][2], d[1][2], d[0][2]




    elif dir == 'F':
        if rotate_dir == '+':
            inner_rotate(f, rotate_dir)
            u[2][0], u[2][1], u[2][2], r[0][0], r[1][0], r[2][0], d[0][0], d[0][1], d[0][2], l[0][2], l[1][2], l[2][2] = \
                l[2][2], l[1][2], l[0][2], u[2][0], u[2][1], u[2][2], r[2][0], r[1][0], r[0][0], d[0][0], d[0][1], d[0][2]
        else:
            inner_rotate(f, rotate_dir)
            u[2][0], u[2][1], u[2][2], r[0][0], r[1][0], r[2][0], d[0][0], d[0][1], d[0][2], l[0][2], l[1][2], l[2][2] = \
                r[0][0], r[1][0], r[2][0], d[0][2], d[0][1], d[0][0], l[0][2], l[1][2], l[2][2], u[2][2], u[2][1], u[2][0]



    elif dir == 'B':
        if rotate_dir == '+':
            inner_rotate(b, rotate_dir)
            l[0][0], l[1][0], l[2][0], u[0][0], u[0][1], u[0][2], r[0][2], r[1][2], r[2][2], d[2][0], d[2][1], d[2][2] = \
                u[0][2], u[0][1], u[0][0], r[0][2], r[1][2], r[2][2], d[2][2], d[2][1], d[2][0], l[0][0], l[1][0], l[2][0]
        else:
            inner_rotate(b, rotate_dir)
            l[0][0], l[1][0], l[2][0], u[0][0], u[0][1], u[0][2], r[0][2], r[1][2], r[2][2], d[2][0], d[2][1], d[2][2] = \
                d[2][0], d[2][1], d[2][2], l[2][0], l[1][0], l[0][0], u[0][0], u[0][1], u[0][2], r[2][2], r[1][2], r[0][2]


for _ in range(tc):
    u = [['w' for i in range(3)] for j in range(3)]
    d = [['y' for i in range(3)] for j in range(3)]
    f = [['r' for i in range(3)] for j in range(3)]
    b = [['o' for i in range(3)] for j in range(3)]
    l = [['g' for i in range(3)] for j in range(3)]
    r = [['b' for i in range(3)] for j in range(3)]

    n = int(input())
    order = input().strip()
    for i in range(0, 3*n, 3):
        dir, rotate_dir = order[i], order[i+1]
        rotate(dir, rotate_dir)

    for result in u:
        print(''.join(result))