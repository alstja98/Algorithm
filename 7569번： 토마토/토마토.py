#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7569                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7569                           #+#        #+#      #+#     #
#    Solved: 2025/01/12 11:20:50 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
readl = sys.stdin.readline

C,R,H = map(int, readl().split())
box = [ [list(map(int, readl().split())) for _ in range(R)] for _ in range(H) ]
visited = [ [[float('inf')]*C for _ in range(R)] for _ in range(H) ]
move_pos = [(-1,0,0), (1,0,0), (0,-1,0), (0,0,1), (0,1,0), (0,0,-1)]
queue = deque([])
for h in range(H):
    for r in range(R):
        for c in range(C):
            if box[h][r][c] == 1:
                queue.append( (h,r,c, 0) )
                visited[h][r][c] = 0
            elif box[h][r][c] == -1:
                visited[h][r][c] = 0

while queue:
    ch, cr, cc, cday = queue.popleft()
    
    for dh, dr, dc in move_pos:
        nh, nr, nc = ch+dh, cr+dr, cc+dc
        if 0<=nh<H and 0<=nr<R and 0<=nc<C and box[nh][nr][nc] != -1 and visited[nh][nr][nc] > cday+1:
            visited[nh][nr][nc] = cday+1
            queue.append( (nh,nr,nc,cday+1) )

ans = 0
for height in visited:
    for row in height:
        if float('inf') in row:
            print(-1)
            sys.exit()
        else:
            ans = max(ans, max(row))

print(ans)
