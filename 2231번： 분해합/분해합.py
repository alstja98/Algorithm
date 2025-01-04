#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2231                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2231                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 11:43:05 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
n = int(readl().strip())
ans = 0

for i in range(1,n):
    str_num = str(i)
    temp_num = i
    for item in list(str_num):
        temp_num += int(item)
    
    if temp_num == n:
        ans = i
        break


print(ans)
    
