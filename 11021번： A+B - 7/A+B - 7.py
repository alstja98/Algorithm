#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11021                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11021                          #+#        #+#      #+#     #
#    Solved: 2025/01/01 14:00:39 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
case = int(readl())
for i in range(1,case+1):
    a,b = map(int, readl().split())
    print(f'Case #{i}: {a+b}')