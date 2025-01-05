#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10815                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10815                          #+#        #+#      #+#     #
#    Solved: 2025/01/04 15:34:57 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
n = int(readl().strip())
my_card = list(map(int, readl().split()))
m = int(readl().strip())
t_card = list(map(int, readl().split()))

hash = {key:1 for key in my_card}
ans = []
for target in t_card:
    if target in hash:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)