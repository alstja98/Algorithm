#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 6087                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/6087                           #+#        #+#      #+#     #
#    Solved: 2025/01/11 15:57:51 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from heapq import heappush, heappop
readl = sys.stdin.readline

C,R = map(int, readl().split()) # C,R 
m = [ list(map(str, readl().strip())) for _ in range(R)]

# 위치, 방향, 거울 사용 횟수, 이동거리 tracking
move_pos = [(-1,0),(0,1),(1,0),(0,-1)] # index = 북(0), 동(1), 남(2), 서(3)
c_pos = []
for i in range(R):
    for j in range(C):
        if m[i][j] == 'C':
            c_pos.append((i,j))

# visited[r][c][d] -> 특정 위치에 특정 방향으로 도달할 때 '거울 사용횟수'를 관리함.
visited = [ [[float('inf')] * 4 for _ in range(C)] for _ in range(R) ]
queue = []
for dir in range(4):
    heappush(queue, (0, c_pos[0][0], c_pos[0][1], dir)) # 거울사용횟수, r,c,방향,이동거리, 처음 이동인지
    visited[c_pos[0][0]][c_pos[0][1]][dir] = 0

while queue:
    cmc, cr, cc, cp = heappop(queue)
    if (cr, cc) == c_pos[1]:
        print(cmc)
        sys.exit()

    for dir, (dr, dc) in enumerate(move_pos):
        nr, nc = cr+dr, cc+dc
        new_cmc = cmc + (1 if dir != cp else 0)
        if 0<=nr<R and 0<=nc<C and m[nr][nc]!='*' and visited[nr][nc][dir] > new_cmc:
            visited[nr][nc][dir] = new_cmc
            heappush(queue, (new_cmc, nr,nc,dir))
                        