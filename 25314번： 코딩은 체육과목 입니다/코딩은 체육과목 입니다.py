#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25314                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25314                          #+#        #+#      #+#     #
#    Solved: 2025/01/01 13:02:18 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 

readl = sys.stdin.readline

n = int(readl())

long_str = 'long ' * (n//4)
print(f'{long_str}int')