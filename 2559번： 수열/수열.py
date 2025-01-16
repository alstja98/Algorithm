#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2559                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2559                           #+#        #+#      #+#     #
#    Solved: 2025/01/12 20:40:41 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
N,K = map(int, readl().split())
nums = list(map(int, readl().split()))

S = [[0] for _ in range(N)]
S[0]=nums[0]
for i in range(1, N):
    S[i] = S[i-1] + nums[i]

ans = -float('inf')
for i in range(K-1,N):
    if i==K-1:
        ans = max(ans, S[i])
    else:
        ans = max(ans, S[i]-S[i-K])

print(ans)