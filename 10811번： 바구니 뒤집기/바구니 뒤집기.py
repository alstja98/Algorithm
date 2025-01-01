#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10811                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10811                          #+#        #+#      #+#     #
#    Solved: 2025/01/01 15:34:54 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

readl = sys.stdin.readline

N, M = map(int, readl().split())

orig_list = [ i+1 for i in range(N) ]
for _ in range(M):
    i, j = map(int, readl().split())
    # list.reverse() 는 리스트 원본을 역순시키고, 반환값은 None 이다.
    # reversed(list) 는 리스트 원본은 유지하고, 새로운 리스트를 반환한다.
    range_list = orig_list[i-1:j]
    range_list.reverse()
    index_list = [ index for index in range(i-1, j)]
    for index, target_item in zip(index_list, range_list):
        orig_list[index] = target_item
    
print(*orig_list)
    
    
    