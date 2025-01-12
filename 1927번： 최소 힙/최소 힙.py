#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1927                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1927                           #+#        #+#      #+#     #
#    Solved: 2025/01/12 17:50:22 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import heapq

input = sys.stdin.readline

def min_heap():
    n = int(input())  
    heap = [] 
    
    for _ in range(n):
        x = int(input())
        if x == 0:
            # 힙이 비어있는 경우 0 출력
            if not heap:
                print(0)
            else:
                print(heapq.heappop(heap))
        else:
            heapq.heappush(heap, x)

if __name__ == "__main__":
    min_heap()