#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2563                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2563                           #+#        #+#      #+#     #
#    Solved: 2025/01/01 18:41:43 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# 도화지 크기 설정
paper = [[0] * 100 for _ in range(100)]

# 색종이 개수 입력
N = int(input())

# 각 색종이의 위치 입력 및 도화지에 표시
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

# 총 면적 계산
total_area = sum(sum(row) for row in paper)
print(total_area)