#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2750                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2750                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 13:48:11 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
tc = int(readl().strip())
arr = []
for _ in range(tc):
    num = int(readl().strip())
    arr.append(num)

for item in sorted(arr):
    print(item)
