#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25305                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25305                          #+#        #+#      #+#     #
#    Solved: 2025/01/04 13:55:50 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
num, k = map(int, readl().split())
arr = list(map(int, readl().split()))
arr.sort(reverse=True)
print(arr[k-1])