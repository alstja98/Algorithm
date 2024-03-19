'''
[ 2024.03.19 화요일 ]

N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.
 
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )
'''

'''
- 슬라이싱 개념
arr = [4,5,6,7,8,9]
arr[1:3]  #[5,6]
arr[:3]  #[4,5,6]
arr[1:]  #[5,6,7,8,9]
arr[:]   #[4,5,6,7,8,9]
'''

'''
- 리스트 관련 메소드
len() 원소 개수 -> len([2,3,4]) -> 3개
[1,2,3] + [4,5] == [1,2,3,4,5]
[1,2] * 2 == [1,2,1,2]
a = [3,1,2] -> print(sorted(a)) -> [1,2,3]
a = [1,2] -> a.append(3) -> [1,2,3]
a = [3,4,5] -> a.insert(1,9) -> [3,9,4,5]
a = [3,4,5] -> a.pop(1) -> [3,5]  #특정 index 항목 삭제
a = [3,4,5] -> a.remove(4) -> [3,5]  #특정 값 삭제
a = [9,4,4,9,5,9] -> a.count(9) == 3  # 일치하는 값의 개수

- 리스트 함축
mylist = [2,3,4,5,6]
new_list = [i for i in mylist if i%2 == 0]   == [2,4,6]
'''

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    min = sum(numbers[:M])  # point 1. 리스트의 요소를 합하여 변수에 넣기
    max = 0

    for i in range(len(numbers) - M+1):
        current_sum = sum(numbers[i:i+M])
        if current_sum > max:
            max = current_sum
        elif current_sum < min:
            min = current_sum
    
    print(f"#{test_case} {max-min}")


