#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11866                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11866                          #+#        #+#      #+#     #
#    Solved: 2025/01/05 18:20:59 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
readl = sys.stdin.readline
N, K = map(int, readl().split())
queue = deque([i for i in range(1,N+1)])

count = 1
ans = []
while queue:
    if count != K:
        front = queue.popleft()
        queue.append(front)
        count += 1
    else:
        front = queue.popleft()
        ans.append(front)
        count = 1
string = ', '.join(map(str, ans))
print(f'<{string}>')
    
    
