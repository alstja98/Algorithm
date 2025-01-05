#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14425                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14425                          #+#        #+#      #+#     #
#    Solved: 2025/01/04 15:45:26 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
n, m = map(int, readl().split())
odict = {str(readl().strip()):1 for _ in range(n)}
count = 0
for _ in range(m):
    target = str(readl().strip())
    if target in odict:
        count += 1
    
print(count)