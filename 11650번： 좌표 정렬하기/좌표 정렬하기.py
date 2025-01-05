#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11650                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11650                          #+#        #+#      #+#     #
#    Solved: 2025/01/04 14:30:17 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
case = int(readl().strip())
arr = []
for _ in range(case):
    x, y = map(int, readl().split())
    arr.append((x,y))

arr.sort(key = lambda x: (x[0], x[1]))
for item in arr:
    x, y = item
    print(x, y)
