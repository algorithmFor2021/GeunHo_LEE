# 합에대한 세그먼트 트리 구성
# 쿼리 -> 업데이트 -> 쿼리 반복
# 리프노드부터 업데이트하는 방식

from math import log2, ceil
import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, q = map(int, input().split())
lst = list(map(int, input().split()))
h = int(ceil(log2(n)))
t_size = 1 << (h+1)
tree = [0 for i in range(t_size)]
operator = deque()
for i in range(q):
    operator.append(list(map(int, input().split())))


def make_segment(index, start, end):
    if start is end:
        tree[index] = lst[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = make_segment(2*index, start, mid) + make_segment(2*index+1, mid+1, end)
    return tree[index]


def query(start, end, index, query_left, query_right):
    if query_left > end or query_right < start:
        return 0
    if query_left <= start and end <= query_right:
        return tree[index]
    mid = (start + end) // 2
    return query(start, mid, 2*index, query_left, query_right) + query(mid+1, end, 2*index+1, query_left, query_right)


def update(new_idx, new_val, index, update_left, update_right):
    if new_idx < update_left or update_right < new_idx:
        return tree[index]
    if update_right is update_left:
        tree[index] = new_val
        return tree[index]
    mid = (update_right + update_left) // 2
    tree[index] = update(new_idx, new_val, 2*index, update_left, mid) + update(new_idx, new_val, 2*index+1, mid+1, update_right)
    return tree[index]


make_segment(1, 0, n-1)

while operator:
    oper = operator.popleft()
    if oper[0] < oper[1]:
        print(query(0, n-1, 1, oper[0]-1, oper[1]-1))
    else:
        print(query(0, n - 1, 1, oper[1]-1, oper[0]-1))
    update(oper[2]-1, oper[3], 1, 0, n-1)