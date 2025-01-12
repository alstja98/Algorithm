#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10870                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10870                          #+#        #+#      #+#     #
#    Solved: 2025/01/05 20:03:54 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
n = int(readl().strip())
if n == 0:
    print(0)
    sys.exit()
elif n == 1:
    print(1)
    sys.exit()

def fibo(stage, i, j):
    if stage == n:
        return i+j
        
    return fibo(stage+1, i+j, i)

print(fibo(2,1,0))