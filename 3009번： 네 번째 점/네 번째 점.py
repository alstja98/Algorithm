#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3009                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3009                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 10:49:26 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
x_coords = []
y_coords = []

for _ in range(3):
    x, y = map(int, input().split())
    x_coords.append(x)
    y_coords.append(y)

x4 = 0
y4 = 0

for x in x_coords:
    if x_coords.count(x) == 1:
        x4 = x
        break

for y in y_coords:
    if y_coords.count(y) == 1:
        y4 = y
        break

print(x4, y4)