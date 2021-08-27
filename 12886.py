# 세 그룹의 값을 같게하는게 목표
# 1. 크기가 같지 않은 두 그룹 선택
# 2. 큰쪽에서 작은쪽으로 돌 전달(작은쪽의 크기만큼)

a, b, c = map(int, input().split())
record = [set()for i in range(3)] # a, b, c 의 값 내역을 기록해줄 set 을 만듦
# ab 비교시에 b 기준 이미 겪었던 숫자면 추가 - 무한루프 방지
visited_ab = []
# ac 비교시에 c 기준 이미 겪었던 숫자면 추가
visited_ac = []
flag = True


def check(x, y):
    while y != x:
        if y > x:
            y -= x
            x += x
            visited_ab.append(y)
        else:
            x -= y
            y += y
            visited_ab.append(y)
        if y in visited_ab:
            break
    return x, y


while a != b or a != c:
    if a != b:
        # 둘 중 하나라도 겪어보지 못한 숫자여야 한다.
        if a not in record[0] or b not in record[1]:
            record[0].add(a)
            record[1].add(b)
            a, b = check(a, b)
            # 초기화
            visited_ab = []
        else:
            flag = False
            break

    if a != c:
        if a not in record[0] or c not in record[2]:
            record[0].add(a)
            record[2].add(c)
            a, c = check(a, c)
            visited_ac = []
        else:
            flag = False
            break

if flag is True:
    print(1)
else:
    print(0)