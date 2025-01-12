#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11286                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11286                          #+#        #+#      #+#     #
#    Solved: 2025/01/12 17:50:26 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import heapq

input = sys.stdin.readline

def abs_heap():
    n = int(input())  
    heap = []
    
    for _ in range(n):
        x = int(input())
        if x == 0:
            if not heap:
                print(0)
            else:
                print(heapq.heappop(heap)[1])
        else:
            heapq.heappush(heap, (abs(x), x))

if __name__ == "__main__":
    abs_heap()