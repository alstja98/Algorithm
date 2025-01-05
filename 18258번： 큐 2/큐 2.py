#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18258                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18258                          #+#        #+#      #+#     #
#    Solved: 2025/01/05 17:26:00 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
readl = sys.stdin.readline

tc = int(readl().strip())
queue = deque([])
for _ in range(tc):
    order = list(map(str, readl().split()))
    case = order[0]
    if case == 'push':
        queue.append(int(order[1]))
    elif case == 'pop':
        if queue:
            tmp = queue.popleft()
            print(tmp)
        else:
            print(-1)
    elif case == 'size':
        print(len(queue))
    elif case == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif case == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif case == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)