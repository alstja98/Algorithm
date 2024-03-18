'''

2024.03.18.월요일
- 리스트에서 최대, 최소를 파악하고 싶을때 max(), min() 함수를 사용하면 된다.
- 리스트에서 중복을 제거하고 싶을 때, Set() 함수를 사용한 후, 다시 리스트로 변환하면 된다.

'''

import sys

#sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split())) # 입력받은 숫자들을 리스트로 변환
    
    max_number = max(numbers)
    min_number = min(numbers)

    difference = max_number - min_number

    print(f"#{test_case} {difference}")
