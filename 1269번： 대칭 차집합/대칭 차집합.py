#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1269                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1269                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 16:52:01 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
a,b = map(int, readl().split())
a_set = set(map(int, readl().split()))
b_set = set(map(int, readl().split()))

a_minus_b = a_set - b_set
b_minus_a = b_set - a_set
ans_set = a_minus_b | b_minus_a
print(len(ans_set))