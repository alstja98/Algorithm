#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 19532                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/19532                          #+#        #+#      #+#     #
#    Solved: 2025/01/04 12:16:01 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
a,b,c,d,e,f = map(int, readl().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a*x + b*y == c) and (d*x + e*y == f):
            print(x,y)