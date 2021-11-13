# 길이 : 2n -> 윗줄 : 1 ~ n , 아랫줄 : n+1 ~ 2n
# 2n 도착시 1로 이동
# 로봇이 올라가는 칸 - conv[0], 내려가는 칸 - conv[n-1] 정해져 있음
# 로봇이 올라가거나 한칸씩 이동할때 마다 내구도 1 감소
# 내구도 0 인 곳에는 로봇 못올라감

# 동작
# 벨트 한칸 이동후 같은방향으로 로봇 한칸 이동
# 1. 이동하려는 방향에 로봇이 있거나 2. 이동하려는 칸의 내구도가 0 이면 못 움직임
# 올라가는 위치(1번 - conv[0])에 로봇이 없다면 로봇을 하나 올린다??
# 내구도가 0인 칸이 K개 이상이 되면 과정 종료 -> 몇번째 진행중이었는지 출력

# 2n 칸 배열을 만들고 각 요소를 리스트로 지정 -> 0인 요소가 k 개 이상이면 종료
# 로봇이 도착할때마다 -1 씩 하고 0 이되면 못오는 조건 설정
import copy
import sys

n, k = map(int, sys.stdin.readline().split())
conv = list(map(int, sys.stdin.readline().split())) # conv 의 각 요소를(내구도, 로봇탑승여부) 이렇게 구성해도 될 듯
move = [0] * (2*n)
cnt = 0
cycle = 0
robot = [0] * n # 로봇이 입장해 있는 칸

while True:
    cycle += 1

    # tmp = copy.deepcopy(move) # 컨베이어 회전용 임시 리스트
    # for i in range(2*n - 1):
    #     tmp[i+1] = conv[i]
    # tmp[0] = conv[2*n - 1]
    # for i in range(2*n):
    #     conv[i] = tmp[i] # 벨트 회전
    #
    tmp1 = conv.pop(-1)
    conv.insert(0, tmp1)

    tmp = copy.deepcopy(move)  # 로봇 이동용 임시 리스트
    for idx, i in enumerate(robot):
        if i == 1: # 로봇이 발견된 칸 기준
            tmp[idx] -= 1 # 본인 칸 비워주고
            tmp[idx+1] += 1 # 다음칸으로 이동 (사실 컨베이어 벨트가 이동하는 거임)

    for i in range(n): # 컨베이어 이동에 맞춰서 로봇 이동
        robot[i] += tmp[i]
    if robot[n-1] == 1: # 로봇이 n 번째 칸에 도착하면
        robot[n-1] = 0  # 로봇 내려줌

    # 2
    for i in range(n-2, -1, -1): # 로봇은 뒤에서 부터 확인
        if robot[i] == 1 and robot[i+1] == 0 and conv[i+1] > 0:
            robot[i+1] = 1
            robot[i] = 0
            conv[i+1] -= 1
            if conv[i+1] == 0:
                cnt += 1
    if robot[n-1] == 1:
        robot[n-1] = 0

    # 3
    if robot[0] == 0 and conv[0] > 0:
        robot[0] = 1
        conv[0] -= 1
        if conv[0] == 0:
            cnt += 1

    # 4
    if cnt >= k:
        break

print(cycle)

# tmp = copy.deepcopy(move) # 로봇 이동용 임시 리스트
#         pass
#
#
# for idx,i in enumerate(robot): # 앞에서부터 확인하면 안됨 -> 뒤에서 부터 확인하도록 다시
#     if i == 1 and robot[idx+1] == 0 and conv[idx+1] > 0: # 로봇이 발견된 칸 기준 : 앞 칸이 비어있고 내구도가 남아있다면
#         tmp[idx] -= 1
#         tmp[idx+1] += 1
#         conv[idx+1] -= 1 # 내구도 감소
#         if conv[idx+1] == 0:
#             cnt += 1
#
# for i in range(n):
#     robot[i] += tmp[i]

    # step += 1 # 2 단계 진행 시작
    #
    # tmp = copy.deepcopy(robot) # 로봇 이동용 임시 리스트
    # for idx,i in enumerate(robot):
    #     if i == 1 and robot[idx+1] == 0 and conv[idx+1] > 0: # 로봇이 발견된 칸 기준 : 앞 칸이 비어있고 내구도가 남아있다면
    #         tmp[idx] -= 1
    #         tmp[idx+1] += 1
    #         conv[idx+1] -= 1 # 내구도 감소
    #         if conv[idx+1] == 0:
    #             cnt += 1
    #
    #
    #
    #
    #
    #
    #
    # step += 1 # 2단계 진행 시작 -> 3단계임 , 2단계 먼저 구현해줘야함.
    #
    # if conv[enter] != 0:
    #     conv[enter] -= 1 # 로봇 탑승
    #     if conv[enter] == 0:
    #         cnt += 1
    #
    # if cnt >= k:
    #     break
    #
    # enter -= 1
    # if enter < 0:
    #     enter = 2*n -1 # 0보다 작아지면 다시 처음값

