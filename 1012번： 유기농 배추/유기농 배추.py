#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1012                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1012                           #+#        #+#      #+#     #
#    Solved: 2025/01/12 17:02:55 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
sys.setrecursionlimit(10**6)
readl = sys.stdin.readline

tc = int(readl().strip())

def dfs(r, c, map, move_pos):
    map[r][c] = 0
    
    for dr, dc in move_pos:
        nr,nc = r+dr, c+dc
        if 0<=nr<R and 0<=nc<C and map[nr][nc]==1:
            dfs(nr,nc,map,move_pos)
    
for _ in range(tc):
    C,R,pos = map(int, readl().split())
    grass_map = [ [0] * C for _ in range(R) ]
    move_pos = [(-1,0), (0,1), (1,0), (0,-1)]
    grass_pos = []

    for _ in range(pos):
        c, r = map(int, readl().split())
        grass_map[r][c] = 1
        grass_pos.append((r,c))
    
    ans = 0
    for grass in grass_pos:
        cr, cc = grass
        if grass_map[cr][cc]==1:
            dfs(cr,cc, grass_map, move_pos)
            ans += 1
    
    print(ans)
            
