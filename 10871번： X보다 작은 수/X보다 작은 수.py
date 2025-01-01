#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10871                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10871                          #+#        #+#      #+#     #
#    Solved: 2025/01/01 14:26:46 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

readl = sys.stdin.readline

length, target = map(int, readl().split())
total_list = list(map(int, readl().split()))
ans_list = list(filter(lambda item: item < target, total_list))
print(*ans_list)