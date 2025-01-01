#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10810                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10810                          #+#        #+#      #+#     #
#    Solved: 2025/01/01 14:39:40 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline

N, M = map(int, readl().split())
ans_list = [0 for _ in range(N)]
for _ in range(M):
    i, j, target = map(int, readl().split())
    for index in range(i-1, j):
        ans_list[index] = target


print(*ans_list)