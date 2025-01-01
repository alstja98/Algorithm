#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5597                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5597                           #+#        #+#      #+#     #
#    Solved: 2025/01/01 14:51:30 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline

total_set = set([i for i in range(1,31)])
comp_list = []
for _ in range(28):
    num = int(readl().strip())
    comp_list.append(num)

new_set = sorted(total_set - set(comp_list))
for item in new_set:
    print(item)