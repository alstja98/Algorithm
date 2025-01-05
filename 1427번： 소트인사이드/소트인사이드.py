#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1427                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1427                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 14:25:21 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl=sys.stdin.readline
num = str(int(readl().strip()))
arr = sorted(list(map(int, num)), reverse=True)
print(''.join(map(str, arr)))