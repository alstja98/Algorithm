#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1929                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1929                           #+#        #+#      #+#     #
#    Solved: 2025/01/05 14:50:36 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import math
import sys
readl = sys.stdin.readline

def is_prime_number(num):
    if num < 2:
        return 0
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    
    return 1

M, N = map(int, readl().split())
for i in range(M, N+1):
    if is_prime_number(i):
        print(i)
    