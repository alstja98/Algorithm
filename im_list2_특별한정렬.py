'''
[24.03.20 목요일]
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.

10 1 9 2 8 3 7 4 6 5

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
'''

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    reversed_A = sorted(A, reverse=True)

    sol = []

    for i in range(0,10):
        if i % 2 == 0:
            sol.append(reversed_A[i//2])
        elif i % 2 == 1:
            sol.append(reversed_A[N-1 - i//2])

    print(f"#{test_case} ", ' '.join(map(str, sol)))  # point 1. 리스트 요소를 문자열로 쭉 뿌리는 방법