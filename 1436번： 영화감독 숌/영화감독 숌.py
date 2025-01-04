#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1436                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1436                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 13:14:42 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
n = int(readl().strip())
count = 0
for i in range(10000000):
    str_i = str(i)
    if '666' in str_i:
        count += 1
    
    if count == n:
        print(i)
        break