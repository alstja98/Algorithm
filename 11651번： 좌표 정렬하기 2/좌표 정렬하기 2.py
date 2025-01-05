#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11651                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11651                          #+#        #+#      #+#     #
#    Solved: 2025/01/04 14:36:26 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
case = int(readl().strip())
arr = []
for _ in range(case):
    x, y = map(int, readl().split())
    arr.append((x,y))

arr.sort(key = lambda x: (x[1], x[0]))
for item in arr:
    x, y = item
    print(x, y)