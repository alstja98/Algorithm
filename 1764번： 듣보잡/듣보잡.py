#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1764                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1764                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 16:42:44 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
n,m = map(int, readl().split())
n_set = set()
m_set = set()
for _ in range(n):
    n_set.add(str(readl().strip()))

for _ in range(m):
    m_set.add(str(readl().strip()))

intersection_set = sorted(n_set & m_set)

print(len(intersection_set))
for item in intersection_set:
    print(item)