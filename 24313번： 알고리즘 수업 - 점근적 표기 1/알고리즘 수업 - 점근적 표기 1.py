#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 24313                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/24313                          #+#        #+#      #+#     #
#    Solved: 2025/01/04 11:35:55 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
a1, a2 = map(int, input().split())
c = int(input())
n = int(input())
if (a1*n + a2) <= (c*n) and a1 <= c:
    print(1)
else:
    print(0)
