#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10809                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10809                          #+#        #+#      #+#     #
#    Solved: 2025/01/01 16:31:18 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
string = list(map(str, readl().strip()))
alpha_list = [chr(code) for code in range(97,123)]
ans_list = []
for item in alpha_list:
    is_none = True
    for index, str_item in enumerate(string):
        if str_item == item:
            ans_list.append(index)
            is_none = False
            break
        
    if is_none == True:
        ans_list.append(-1)
        
print(*ans_list)
    
