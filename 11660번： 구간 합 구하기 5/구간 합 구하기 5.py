#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11660                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11660                          #+#        #+#      #+#     #
#    Solved: 2025/01/12 20:41:02 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
N, M = map(int, readl().split())
table = [list(map(int,readl().split())) for _ in range(N)]
S = [[0] * (N + 1) for _ in range(N + 1)]
# S 배열 계산
for r in range(1, N + 1):
    for c in range(1, N + 1):
        S[r][c] = table[r - 1][c - 1] + S[r - 1][c] + S[r][c - 1] - S[r - 1][c - 1]

for _ in range(M):
    r1, c1, r2, c2 = map(int, readl().split())
    result = S[r2][c2] - S[r1 - 1][c2] - S[r2][c1 - 1] + S[r1 - 1][c1 - 1]
    print(result)