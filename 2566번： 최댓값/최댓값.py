#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2566                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2566                           #+#        #+#      #+#     #
#    Solved: 2025/01/01 18:20:33 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

readl = sys.stdin.readline

matrix = [ list(map(int, readl().split())) for _ in range(9) ]

max_value = 0
ans_row, ans_col = 0,0
for r_index, row in enumerate(matrix):
    for c_index, col in enumerate(row):
        if col >= max_value:
            max_value = col
            ans_row, ans_col = r_index, c_index
    
print(max_value)
print(f'{ans_row+1} {ans_col+1}')