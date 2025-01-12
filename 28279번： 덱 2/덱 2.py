#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 28279                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/28279                          #+#        #+#      #+#     #
#    Solved: 2025/01/05 18:21:18 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
readl = sys.stdin.readline
tc = int(readl().strip())
queue = deque()
for _ in range(tc):
    order = list(map(int, readl().split()))
    
    first = order[0]
    if first == 1:
        queue.appendleft(order[1])
    elif first == 2:
        queue.append(order[1])
    elif first == 3:
        if queue:
            item = queue.popleft()
            print(item)
        else:
            print(-1)
    elif first == 4:
        if queue:
            item = queue.pop()
            print(item)
        else:
            print(-1)
    elif first == 5:
        print(len(queue))
    elif first == 6:
        if queue:
            print(0)
        else:
            print(1)
    elif first == 7:
        if queue:
            print(queue[0])       
        else:
            print(-1)
    elif first == 8:
        if queue:
            print(queue[-1])
        else:
            print(-1)