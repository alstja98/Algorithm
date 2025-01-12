#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14888                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14888                          #+#        #+#      #+#     #
#    Solved: 2025/01/09 22:49:31 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from itertools import permutations

readl = sys.stdin.readline
N = int(readl())
num = list(map(int, readl().split()))
op_num = list(map(int, readl().split()))  # +, -, *, /
op_list = ['+', '-', '*', '/']
op = []

for k in range(len(op_num)):
    for i in range(op_num[k]):
        op.append(op_list[k])

max_value = -float('inf')
min_value = float('inf')


for tc in permutations(op, N - 1):
    total = num[0]
    for r in range(1, N):
        if tc[r - 1] == '+':
            total += num[r]
        elif tc[r - 1] == '-':
            total -= num[r]
        elif tc[r - 1] == '*':
            total *= num[r]
        elif tc[r - 1] == '/':
            total = int(total / num[r])

    max_value = max(max_value, total)
    min_value = min(min_value, total)

print(max_value)
print(min_value)