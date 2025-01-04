#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10798                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10798                          #+#        #+#      #+#     #
#    Solved: 2025/01/01 18:26:09 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline

matrix = [ list(map(str, readl().strip())) for _ in range(5) ]
for r_index, row in enumerate(matrix):
    row_count = len(row)
    if row_count <= 15:
        space = [' ' for _ in range(15 - row_count)]
        matrix[r_index] = row + space

ans = ''
for col in zip(*matrix):
    for col_item in col:
        if col_item != ' ':
            ans += col_item

print(ans)