#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15552                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15552                          #+#        #+#      #+#     #
#    Solved: 2025/01/01 13:58:36 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

readl = sys.stdin.readline

case = int(readl())
for _ in range(case):
    a, b = map(int, readl().split())
    print(a+b)