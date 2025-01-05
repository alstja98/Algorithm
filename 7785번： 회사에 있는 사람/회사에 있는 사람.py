#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7785                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7785                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 15:59:11 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
tc = int(readl().strip())
log = {}
for _ in range(tc):
    name, check = map(str, readl().split())
    log[name] = check

ans = []
for name, check in log.items():
    if check == 'enter':
        ans.append(name)

for item in sorted(ans, reverse=True):
    print(item)