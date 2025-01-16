#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11659                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11659                          #+#        #+#      #+#     #
#    Solved: 2025/01/12 20:16:13 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline

N, tc = map(int, readl().split())
nums = list(map(int, readl().split()))
S = [0] * (N+1)
for i in range(1, N+1):
    S[i] = S[i-1] + nums[i-1]
    
for _ in range(tc):
    i, j = map(int, readl().split())
    print(S[j]-S[i-1])