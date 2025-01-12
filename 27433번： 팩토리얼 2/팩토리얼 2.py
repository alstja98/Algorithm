#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 27433                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/27433                          #+#        #+#      #+#     #
#    Solved: 2025/01/05 19:48:10 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
num = int(readl().strip())
if num == 0 or num == 1:
    print(1)
    sys.exit()

ans = 1
def factorial(n):
    global ans
    if n < 2:
        return 
    
    ans *= n
    return factorial(n-1)

factorial(num)
print(ans)