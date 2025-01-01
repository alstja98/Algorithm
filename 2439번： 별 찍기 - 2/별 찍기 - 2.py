#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2439                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2439                           #+#        #+#      #+#     #
#    Solved: 2025/01/01 14:06:18 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline

num=int(readl())
for i in range(1,num+1):
    space = ' ' * (num-i)
    star = '*'*i
    print(f'{space}{star}')