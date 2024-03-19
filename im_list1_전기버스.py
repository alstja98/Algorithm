'''
[2024.03.18.월요일]

A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
'''

T = int(input())

for test_case in range(1, T + 1):
    K,N,M = map(int, input().split())
    stations = list(map(int, input().split()))

    current_position = 0 # point 1) 특정 루트를 이동할 때, 현재 위치 변수
    charge_count = 0

    while current_position + K < N: # point 2) 목표지점까지 도달해야할 떄, for 보다는 while로.
        for move in range(K,0,-1): # point 3) 최대 이동 거리에 한계를 두는 방법
            if current_position + move in stations :
                current_position += move
                charge_count += 1
                break
        else:
            charge_count = 0
            break
        
        '''
        for 루프가 중간에 break 문으로 인해 중단되지 않고 정상적으로 모든 반복을 완료했을 때만 else 블록이 실행됩니다.
        이는 주로 루프를 통해 어떤 조건을 검사하고, 해당 조건이 루프 내 어디에서도 만족하지 않았을 때만 추가적인 작업을 수행하고자 할 때 유용합니다.
        '''
        
        print(f"#{test_case} {charge_count}")