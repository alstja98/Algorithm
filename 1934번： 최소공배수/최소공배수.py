#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1934                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1934                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 17:38:20 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
tc = int(readl().strip())

def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a

# 최소 공배수 = a*b / 최대공약수
for _ in range(tc):
    a, b = map(int, readl().split())
    print(int(a*b/gcd(a,b)))