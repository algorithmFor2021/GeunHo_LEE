# 가로등을 켜 두면 하루에 길의 미터 수만큼 돈이 들어감
# 도시에 있는 모든 두 집 쌍에 대해, 불이 켜진 길만으로 서로를 왕래할 수 있어야 한다
# 집의 수 : tc[0], 길의 수 : tc[1]
# 즉 싸이클이 발생하지 않게 모든 집들이 하나의 간선으로 이루어지게 만들며 됨.

tc = list(map(int, input().split()))


# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을때까지 재귀 호출
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


while tc[0] != 0 and tc[1] != 0:
    n, m = tc
    # 모든 간선을 담을 리스트, 최종 비용을 담을 변수
    edges = []
    origin_cost = 0
    fit_cost = 0
    # 부모 테이블 - 노드의 갯수 만큼
    parent = [0] * (n + 1)
    # 부모테이블상 부모를 자기 자신으로 초기화
    for i in range(1, n+1):
        parent[i] = i
    for i in range(m):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))
    # 간선을 비용순으로 정렬
    edges.sort()

    for edge in edges:
        cost, a, b = edge
        origin_cost += cost
        # 사이클이 발생하지 않을 경우(같은 부모를 같지 않는경우)
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            fit_cost += cost
    result = origin_cost - fit_cost
    print(result)

    tc = list(map(int, input().split()))