#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2720                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2720                           #+#        #+#      #+#     #
#    Solved: 2025/01/02 20:21:30 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
test_case = int(readl().strip())
for _ in range(test_case):
    money_list = [25, 10, 5, 1]
    ans_list = [0,0,0,0]
    target_money = int(readl().strip())
    while target_money != 0:
        for index, money in enumerate(money_list):
            target_money -= money
            if target_money < 0:
                target_money += money
                continue
            else:
                ans_list[index] += 1
                break
    
    print(*ans_list)