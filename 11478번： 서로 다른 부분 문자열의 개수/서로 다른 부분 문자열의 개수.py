#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11478                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11478                          #+#        #+#      #+#     #
#    Solved: 2025/01/04 17:00:42 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from itertools import combinations
import sys
readl = sys.stdin.readline
string = str(readl().strip())
length = len(string)
substring = set()
for i in range(length):
    for j in range(i+1, length+1):
        substring.add(string[i:j])

print(len(substring))
