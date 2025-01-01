#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2675                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2675                           #+#        #+#      #+#     #
#    Solved: 2025/01/01 16:51:52 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
case_num = int(readl())
for _ in range(case_num):
    mul, string = map(str, readl().split())
    mul = int(mul)
    ans_str = ''
    for item in string:
        ans_str += item*mul
    
    print(ans_str)
    