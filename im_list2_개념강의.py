'''
[2024.03.19 화요일]

1. 2차원 리스트 입력 받기
    n,m = map(int, input.split())
    mylist = [list(map(int, input().split())) for _ in range(n)]


2. 리스트 순회
 (1) 행 우선 순회
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j]

 (2) 열 우선 순회
    for j in range(len(arr[0]))
        for i in range(len(arr)):
            arr[i][j]

 (3) 델타를 이용한 2차 리스트 탐색
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            for i in range(4):
                testX = x + dx[i]
                textY = y + dy[i]
                print(arr[textX][textY])        

3. zip 메소드 : 동일한 개수로 이루어진 자료형들을 묶어주는 역할을 하는 함수
    alpha = ['a','b','c']
    index = [1,2,3]
    alph_index = list(zip(alpha, index))
    print(alph_index)  == [('a',1),('b',2),('c',3)]
'''