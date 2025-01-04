#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5073                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5073                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 11:11:26 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    
    sides = sorted([a, b, c])
    a, b, c = sides
    
    if c >= a + b:
        print("Invalid")
    else:
        if a == b == c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")