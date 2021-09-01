from collections import deque
from math import log2, ceil
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
h = int(ceil(log2(n)))
t_size = 1 << (h + 1)
min_tree = [0 for i in range(t_size)]
max_tree = [0 for i in range(t_size)]
lst = []
operator = deque()
for i in range(n):
    lst.append(int(input()))
for i in range(m):
    operator.append(list(map(int, input().split())))


def min_init(start, end, index):
    if start is end:
        min_tree[index] = lst[start]
        return min_tree[index]
    mid = (start + end) // 2
    min_tree[index] = min(min_init(start, mid, 2*index), min_init(mid+1, end, 2*index+1))
    return min_tree[index]


def max_init(start, end, index):
    if start is end:
        max_tree[index] = lst[start]
        return max_tree[index]
    mid = (start + end) // 2
    max_tree[index] = max(max_init(start, mid, 2*index), max_init(mid+1, end, 2*index+1))
    return max_tree[index]


def min_query(start, end, index, query_left, query_right):
    if end < query_left or start > query_right:
        return sys.maxsize # min 값을 찾아주는 거라 0 리턴하면 안됨
    if query_left <= start and end <= query_right:
        return min_tree[index]
    mid = (start + end) // 2
    return min(min_query(start, mid, 2*index, query_left, query_right), min_query(mid+1, end, 2*index+1, query_left, query_right))


def max_query(start, end, index, query_left, query_right):
    if end < query_left or start > query_right:
        return 0
    if query_left <= start and end <= query_right:
        return max_tree[index]
    mid = (start + end) // 2
    return max(max_query(start, mid, 2*index, query_left, query_right), max_query(mid+1, end, 2*index+1, query_left, query_right))


min_init(0, n-1, 1)
max_init(0, n-1, 1)

while operator:
    a, b = operator.popleft()
    print("{} {}".format(min_query(0, n-1, 1, a-1, b-1), max_query(0, n-1, 1, a-1, b-1)))