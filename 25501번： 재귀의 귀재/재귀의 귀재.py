#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25501                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25501                          #+#        #+#      #+#     #
#    Solved: 2025/01/05 20:18:55 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
tc = int(readl().strip())

def recursion(s, l, r, count):
    if l >= r: return (1, count)
    elif s[l] != s[r]: return (0, count)
    else: return recursion(s, l+1, r-1, count+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

for _ in range(tc):
    es = str(readl().strip())
    isPal, count = isPalindrome(es)
    print(isPal, count)
    
    