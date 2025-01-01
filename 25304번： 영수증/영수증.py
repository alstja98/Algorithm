#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25304                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25304                          #+#        #+#      #+#     #
#    Solved: 2025/01/01 12:48:53 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

readl = sys.stdin.readline

total = int(readl())
num = int(readl())

temp_total = 0
for _ in range(num):
    p, c = map(int, readl().split())
    temp_total += p*c

if temp_total == total:
    print('Yes')
else:
    print('No')