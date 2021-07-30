# i <= j
# 모든 부배열의 합을 구한다? - 9% 시간초과
# 모든 부배열 리스트의 이중 for 문 제거 -> dictionary 이용 - 여전히 9% 시간초과
# dictionary 에 값을 집어넣는 부분에도 매번 분기가 걸리니까 defaultdict 를 이용하면 시간을 줄일수 있다. - 9% 시간초과
# 맨 마지막 result 를 구할 때 A, B 두 key 값에 대한 이중 for 문을 돌리지 말고 A[i] * B[t - i] 로 단일 for 문 처리 - 통과
from collections import defaultdict

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))


# 전체 부분합 구하는 함수
def part_sum(lst):
    # key 에 맞는 value 가 없으면 0 이 들어감.
    tmp = defaultdict(int)
    for j in range(len(lst)):
        total = 0
        for i in range(j, len(lst)):
            total += lst[i]
            tmp[total] += 1

    return tmp


a_part = part_sum(A)
b_part = part_sum(B)

result = 0
for i in a_part.keys():
    result += (a_part[i] * b_part[t - i])
    # for i in b_part.keys():
    #     if j + i == t:
    #        result += (a_part[j] * b_part[i])
print(result)