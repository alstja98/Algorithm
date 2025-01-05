#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10773                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10773                          #+#        #+#      #+#     #
#    Solved: 2025/01/04 17:54:28 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
readl = sys.stdin.readline
tc = int(readl().strip())
nums = []
for _ in range(tc):
    num = int(readl().strip())
    if num != 0:
        nums.append(num)
    else:
        nums.pop()

print(sum(nums))