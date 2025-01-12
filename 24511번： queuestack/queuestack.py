#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 24511                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/24511                          #+#        #+#      #+#     #
#    Solved: 2025/01/05 18:21:29 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
readl = sys.stdin.readline

qs_len = int(readl().strip())
qs_kind = list(map(int, readl().split()))
qs_item = list(map(int, readl().split()))

insert_len = int(readl().strip())
insert_item = list(map(int, readl().split()))

ans = []
dq = deque()
for index, item in enumerate(qs_item):
    if qs_kind[index] == 0:
        dq.append(item)

for insert in insert_item:
    dq.appendleft(insert)
    ans.append(dq.pop())

print(*ans)
