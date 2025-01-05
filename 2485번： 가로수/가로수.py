#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2485                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2485                           #+#        #+#      #+#     #
#    Solved: 2025/01/05 11:38:54 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import math
readl = sys.stdin.readline
tc = int(readl().strip())
trees = [ int(readl().strip()) for _ in range(tc) ]
intervals = [ trees[i] - trees[i-1] for i in range(1, tc) ]
current_gcd = intervals[0]
for interval in intervals[1:]:
    current_gcd = math.gcd(current_gcd, interval)

total_new_trees = 0
for interval in intervals:
    total_new_trees += (interval // current_gcd) - 1

print(total_new_trees)