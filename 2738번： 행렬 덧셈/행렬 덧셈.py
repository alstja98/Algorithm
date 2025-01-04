#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2738                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2738                           #+#        #+#      #+#     #
#    Solved: 2025/01/01 18:11:22 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

readl = sys.stdin.readline

N, M = map(int,readl().split())
A = [ list(map(int, readl().split())) for _ in range(N) ]
B = [ list(map(int, readl().split())) for _ in range(N) ]
C = []
for a_row, b_row in zip(A,B):
    C.append([ a_row[i] + b_row[i] for i in range(M) ])
    
for c_row in C:
    print(*c_row)
        
    