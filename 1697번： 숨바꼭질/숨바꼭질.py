#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1697                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1697                           #+#        #+#      #+#     #
#    Solved: 2025/01/12 17:28:07 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from heapq import heappush, heappop
readl = sys.stdin.readline

subin, target = map(int, readl().split())
queue = []
visited = [False] * (100001)
heappush(queue, (0,subin))

while queue:
    cur_time, cur_pos = heappop(queue)
    if cur_pos == target:
        print(cur_time)
        break
    
    for i in range(3):
        if i == 0:
            next_pos = cur_pos-1
        elif i == 1:
            next_pos = cur_pos+1
        elif i == 2:
            next_pos = 2*cur_pos
        
        if 0<=next_pos<=100000 and not visited[next_pos]:
            visited[next_pos] = True
            heappush(queue, ((cur_time+1, next_pos)))
    
    