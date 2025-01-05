#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2164                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2164                           #+#        #+#      #+#     #
#    Solved: 2025/01/05 18:04:35 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

readl = sys.stdin.readline
n = int(readl().strip())
initial = [i for i in range(1, n+1)]
queue = deque(initial)

stage = 1
while len(queue) != 1:
    if stage % 2 == 1:
        queue.popleft()
    elif stage % 2 == 0:
        front = queue.popleft()
        queue.append(front)
    
    stage += 1

print(queue[0])
        
    

    