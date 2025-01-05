#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18870                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18870                          #+#        #+#      #+#     #
#    Solved: 2025/01/04 14:56:32 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
tc = int(readl().strip())
arr = list(map(int, readl().split()))
sorted_set_arr = sorted(set(arr))
# 각 숫자에 대한 인덱스를 딕셔너리에 저장
mapping = {num: idx for idx, num in enumerate(sorted_set_arr)}
ans = [mapping[num] for num in arr]
print(*ans)
