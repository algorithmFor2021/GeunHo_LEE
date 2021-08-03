# 백트래킹 -> 임의의 집합에서 주어진 기준대로 원소의 순서를 선택하는 문제에 적합
# 유망한지(Promising) 판별하는 함수 필요 -> 아니라면 가지치기(Pruning)
# 같은 행, 같은 열, 같은 대각선에는 놓을 수 없음 -> 총 3가지 제약조건
from timeit import default_timer as timer
start = timer()

n = int(input())
length = 0
# i 번째 행에 몇 번째 열에 퀸을 놓을건지 정해주는 리스트
col = [0] * (n + 1)
# 같은 열에 퀸이 배치 되는지 확인하는 리스트
visited = [False] * (n+1)
result = 0


# 같은 행, 같은 열에 있는지 확인은 이 함수 내에서 처리
def queens(i):
    global result
    # 유망한데 n 까지 도착했다면 배치 성공
    if i == n:
        result += 1
        return
    else:
        # 모든 열 확인
        for j in range(1, n + 1):
            # 같은 열에 퀸이 있다면 배치 불가
            if visited[j]:
                continue
            if promising(i, j):
                visited[j] = True
                col[i] = j
                # 다음 행
                queens(i+1)
                visited[j] = False


# 같은 대각선 내에 있는지 확인
def promising(idx, val):
    global col
    for i in range(idx):
        # 대각선 확인
        if abs(col[i] - val) == abs(i - idx):
            return False
    return True


queens(0)
print(result)
print(timer() - start)