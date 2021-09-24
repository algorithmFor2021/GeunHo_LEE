# 오르막: 점선, 내리막: 실선
# 입구 : 0
# 최대한 내리막이 많게 -> 내리막으로 갔다가 돌아올때 오르막이 되는 경우는 고려x
# 피로도 : 오르막 개수 ** 2

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(1, n+1):
    parent[i] = i

edges = []
worst = 0
best = 0
for i in range(m+1):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# worst 구하기
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        if cost == 0:
            worst += 1
worst = pow(worst, 2)

# best 구하기
for i in range(1, n+1):
    parent[i] = i
edges = sorted(edges, key=lambda x: (-x[0]))
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        if cost == 0:
            best += 1
best = pow(best, 2)

result = worst - best
print(result)