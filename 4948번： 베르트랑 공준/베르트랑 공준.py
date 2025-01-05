#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4948                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4948                           #+#        #+#      #+#     #
#    Solved: 2025/01/05 14:56:01 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import math
readl = sys.stdin.readline

def is_prime_number(num):
    if num < 2 :
        return 0
    
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return 0
        
    return 1
prime_check = [ True if is_prime_number(i) else False for i in range(246913)]

while True:
    tn = int(readl().strip())
    if tn == 0:
        break

    count = 0
    for i in range(tn+1, 2*tn + 1):
        if prime_check[i]:
            count += 1
    
    print(count)