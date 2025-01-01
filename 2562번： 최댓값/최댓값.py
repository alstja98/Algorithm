#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2562                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2562                           #+#        #+#      #+#     #
#    Solved: 2025/01/01 14:36:39 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline

ans_list = []
while True:
    line = readl()
    if not line:
        break
    
    num = int(line)
    ans_list.append(num)
    
max_value = max(ans_list)
print(max_value)
print(ans_list.index(max_value) + 1)
