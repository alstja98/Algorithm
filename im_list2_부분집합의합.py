'''
[24.03.20 수요일]
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
'''

'''
point1. 집합에서 모든 가능한 부분집합을 어떻게 생성할 것인가?
point2. 생성된 각 부분집합에 대해 원소의 합이 K 인지 확인한다.
'''

from itertools import combinations

T = int(input())

for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))

    A = range(1,13) # point3. 1부터 12까지의 숫자로 구성된 집합 A
    count = 0

    for subset in combinations(A, N):  # point1. 집합에서 부분집합을 생성하는 방법
        if sum(subset) == K:  # point2. 부분집합의 합이 K인지 확인하는 방법
            count += 1

    print(f"#{test_case} {count}")