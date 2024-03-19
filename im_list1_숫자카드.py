'''
[2024.03.19 화요일]

0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.
'''

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input()))  #point 1. 공백없이 문자열을 입력받는경우, input().split() 하지 말기
    max_count = 0
    max_number = 0
    
    non_dup_numbers = list(set(numbers)) 
    for i in non_dup_numbers:
        count = numbers.count(i)  # point 2. 일치하는 값의 개수 파악 == count()
        if max_count < count:
            max_count = count
            max_number = i
        elif max_count == count:
            if i > max_number:
                max_number = i
                
    print(f"#{test_case} {max_number} {max_count}")  # 결과 출력
