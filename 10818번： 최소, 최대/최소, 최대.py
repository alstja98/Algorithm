#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10818                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10818                          #+#        #+#      #+#     #
#    Solved: 2025/01/01 14:33:55 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline

num = int(readl())
total_list = list(map(int, readl().split()))
ans_list = [min(total_list), max(total_list)]
print(*ans_list)