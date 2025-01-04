#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10101                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10101                          #+#        #+#      #+#     #
#    Solved: 2025/01/04 11:10:32 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
a = int(input())
b = int(input())
c = int(input())

if a == 60 and b == 60 and c == 60:
    print("Equilateral")
elif a + b + c == 180:
    if a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")