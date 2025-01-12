#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11279                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11279                          #+#        #+#      #+#     #
#    Solved: 2025/01/12 17:50:16 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import heapq

input = sys.stdin.readline

def max_heap():
    n = int(input())  # 입력 횟수
    heap = []  # 최대 힙 (heapq를 이용)
    
    for _ in range(n):
        x = int(input())
        if x == 0:
            # 힙이 비어있는 경우 0 출력
            if not heap:
                print(0)
            else:
                # 최대 힙의 최댓값 출력
                print(-heapq.heappop(heap))
        else:
            # 최대 힙에 값 추가 (음수로 저장)
            heapq.heappush(heap, -x)

if __name__ == "__main__":
    max_heap()