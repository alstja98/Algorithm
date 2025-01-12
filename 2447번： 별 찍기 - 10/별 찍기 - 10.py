#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2447                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2447                           #+#        #+#      #+#     #
#    Solved: 2025/01/05 19:24:45 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
N = int(readl().strip())
star = [[' ' for _ in range(N)] for _ in range(N)]

def make_pattern(n,r,c):
    if n == 1:
        star[r][c] = '*'
        return
    m = n//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            make_pattern(m, r+i*m, c+j*m)


make_pattern(N,0,0)
for row in star:
    print(''.join(row))