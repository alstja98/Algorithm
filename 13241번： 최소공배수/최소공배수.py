#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13241                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13241                          #+#        #+#      #+#     #
#    Solved: 2025/01/04 17:51:17 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline

def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a

# 최소 공배수 = a*b / 최대공약수
a, b = map(int, readl().split())
print(int(a*b/gcd(a,b)))