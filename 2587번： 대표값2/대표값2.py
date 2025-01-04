#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2587                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2587                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 13:53:41 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
arr = []
for _ in range(5):
    num = int(readl().strip())
    arr.append(num)
arr.sort()
print(sum(arr)//5)
print(arr[2])