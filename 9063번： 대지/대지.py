#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9063                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9063                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 11:05:01 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
num = int(readl().strip())
min_x = float('inf')
max_x = -float('inf')
min_y = float('inf')
max_y = -float('inf')

for _ in range(num):
    x, y = map(int, readl().split())
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

print((max_x - min_x)*(max_y - min_y))