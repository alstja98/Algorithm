#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10816                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10816                          #+#        #+#      #+#     #
#    Solved: 2025/01/04 16:34:31 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
n = int(readl().strip())
n_list = list(map(int, readl().split()))
m = int(readl().strip())
m_list = list(map(int, readl().split()))

mine = {}
for item in n_list:
    if item not in mine:
        mine[item] = 1
    else:
        mine[item] += 1

ans = []
for item in m_list:
    if item in mine:
        ans.append(mine[item])
    else:
        ans.append(0)
        
print(*ans)

