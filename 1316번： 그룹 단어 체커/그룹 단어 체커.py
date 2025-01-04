#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1316                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1316                           #+#        #+#      #+#     #
#    Solved: 2025/01/01 17:38:00 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
num = int(readl())
ans = 0

for _ in range(num):
    string = readl().strip()
    
    used_str = []
    for index, item in enumerate(string):
        if item not in used_str:
            if index == (len(string)-1):
                ans+=1
            used_str.append(item)
            continue
        else:
            if item == string[index-1]:
                if index == (len(string)-1):
                    ans+=1
                continue
            else:
                break

print(ans)