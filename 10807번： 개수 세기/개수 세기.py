#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10807                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10807                          #+#        #+#      #+#     #
#    Solved: 2025/01/01 14:18:36 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

readl = sys.stdin.readline
num = int(readl())
list = list(map(int, readl().split()))
target = int(readl())
print(list.count(target))