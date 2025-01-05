#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9012                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9012                           #+#        #+#      #+#     #
#    Solved: 2025/01/05 12:12:48 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
tc = int(readl().strip())
for _ in range(tc):
    case = list(map(str, readl().strip()))
    check = []
    is_print = False
    for item in case:
        if item == '(':
            check.append(item)
        elif item == ')':
            if check:
                check.pop()
            else:
                print('NO')
                is_print = True
                break
    
    if is_print == False:
        if not check:
            print('YES')
        else:
            print('NO')