#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2292                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2292                           #+#        #+#      #+#     #
#    Solved: 2025/01/02 20:54:11 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
n = 0
N = int(readl().strip())
if N==1:
    print(1)
else:
    init_num = 2
    while True:
        n += 1
        if init_num <= N < (init_num + (6*n)):
            break
        else:
            init_num += (6*n)

    print(n+1)