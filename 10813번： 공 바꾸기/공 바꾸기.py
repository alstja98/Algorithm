#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10813                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10813                          #+#        #+#      #+#     #
#    Solved: 2025/01/01 14:47:18 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
readl = sys.stdin.readline
N, M = map(int, readl().split())

ans_list = [i+1 for i in range(N)]
for _ in range(M):
    i, j = map(int, readl().split())
    temp = ans_list[i-1]
    ans_list[i-1] = ans_list[j-1]
    ans_list[j-1] = temp

print(*ans_list)