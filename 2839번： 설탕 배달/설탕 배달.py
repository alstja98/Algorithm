#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2839                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2839                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 13:23:29 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
n = int(readl().strip())

all_simu = [ [5*j + 3*i for i in range(n//3 + 1)] for j in range(n//5 + 1)]
check = False
ans = 0
for r_index, row in enumerate(all_simu):
    for c_index, item in enumerate(row):
        if item == n:
            check = True
            ans = (r_index + c_index)

if check == False:
    print(-1)
else:
    print(ans)