#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16928                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16928                          #+#        #+#      #+#     #
#    Solved: 2025/01/12 11:43:48 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from heapq import heappop, heappush
readl = sys.stdin.readline
N, M = map(int, readl().split())
ladder = {}
for _ in range(N):
    start, end = map(int, readl().split())
    ladder[start] = end
    
snake = {}
for _ in range(M):
    start, end = map(int, readl().split())
    snake[start] = end


visited = [False]*101
visited[1] = True
queue = []
heappush(queue, (-1, 1, 0)) # 현재 위치가 어디고, 주사위 몇번 굴렸는지

ans = 0
while queue:
    minus_pos, pos, count = heappop(queue)
    if pos == 100:
        ans = count
        break

    for num in range(1, 7):
        next_pos = (pos+num)
        if next_pos <= 100:
            if next_pos in ladder:
                next_pos = ladder[next_pos]
            elif next_pos in snake:
                next_pos = snake[next_pos]
            
            if not visited[next_pos]:
                visited[next_pos] = True
                heappush(queue, (-next_pos, next_pos, count+1))

print(ans)