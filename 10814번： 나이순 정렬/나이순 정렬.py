#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10814                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10814                          #+#        #+#      #+#     #
#    Solved: 2025/01/04 14:48:28 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
tc = int(readl())
arr = []
for i in range(tc):
    age, name = map(str, readl().split())
    arr.append((i,age,name))
arr.sort(key=lambda x: (int(x[1]), x[0]))
for item in arr:
    index, age, name = item
    print(age, name)