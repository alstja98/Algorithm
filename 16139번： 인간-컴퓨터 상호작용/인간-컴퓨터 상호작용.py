#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16139                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16139                          #+#        #+#      #+#     #
#    Solved: 2025/01/12 20:40:53 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline

name = str(readl().strip())
tc = int(readl().strip())

alpha_dict = {chr(i):[] for i in range(97, 123)}

for index, item in enumerate(name):
    alpha_dict[item].append(index)
    
for _ in range(tc):
    alpha, l, r = map(str, readl().split())
    l,r = int(l), int(r)
    
    if alpha_dict[alpha]:
        ans = 0
        for index in alpha_dict[alpha]:
            if l<=index<=r:
                ans+=1
        print(ans)
    else:
        print(0)
    