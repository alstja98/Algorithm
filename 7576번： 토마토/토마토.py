#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7576                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7576                           #+#        #+#      #+#     #
#    Solved: 2025/01/11 21:55:03 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
readl = sys.stdin.readline

C,R = map(int, readl().split())
box = [list(map(int, readl().split())) for _ in range(R)]
move_pos = [(-1,0), (0,1), (1,0), (0,-1)]

visited = [[float('inf')] * C for _ in range(R)]
queue = deque([])
for i in range(R):
    for j in range(C):
        if box[i][j] == 1:
            queue.append((i,j,0))
            visited[i][j] = 0
        elif box[i][j] == -1:
            visited[i][j] = 0

while queue:
    cr, cc, cday= queue.popleft()
    
    for dr, dc in move_pos:
        nr, nc = cr+dr, cc+dc
        if 0<=nr<R and 0<=nc<C and box[nr][nc] != -1 and box[nr][nc] != 1 and visited[nr][nc] > cday+1:
            visited[nr][nc] = cday + 1
            queue.append((nr,nc,cday+1))
            
ans = 0
for row in visited:
    if float('inf') in row:
        ans = -1
        break
    else:
        ans = max(ans, max(row))

print(ans)

