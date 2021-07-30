# i <= j
# 모든 부배열의 합을 구한다? - 9% 시간초과
# 모든 부배열 리스트의 이중 for 문 제거 -> dictionary 이용 - 여전히 9% 시간초과
# 문제유형 : 이분탐색 - 어떻게 활용할 것인지?

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))


# 전체 부분합 구하는 함수
def part_sum(lst):
    tmp = dict()
    for j in range(len(lst)):
        total = 0
        for i in range(j, len(lst)):
            total += lst[i]
            if total in tmp.keys():
                cnt = tmp[total]
                tmp[total] = cnt + 1
            else:
                tmp[total] = 1

    return tmp


result = 0
a_part = part_sum(A)
b_part = part_sum(B)

result = 0
for j in a_part.keys():
    for i in b_part.keys():
        if j + i == t:
           result += (a_part[j] * b_part[i])
print(result)