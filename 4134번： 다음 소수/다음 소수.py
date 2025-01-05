#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4134                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4134                           #+#        #+#      #+#     #
#    Solved: 2025/01/05 12:33:41 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import math
readl = sys.stdin.readline
tc = int(readl())
def is_prime_number(num):
    if num < 2:
        return 0
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    
    return 1

for _ in range(tc):
    target = int(readl().strip())
    next_check = target
    while True:
        check = is_prime_number(next_check)
        if check:
            print(next_check)
            break
        else:
            next_check += 1