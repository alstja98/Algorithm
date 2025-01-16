#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1504                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1504                           #+#        #+#      #+#     #
#    Solved: 2025/01/14 21:07:03 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from heapq import heappush, heappop

readl = sys.stdin.readline

N, E = map(int, readl().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    n1, n2, w = map(int, readl().split())
    graph[n1].append((n2, w))
    graph[n2].append((n1, w))
    

    
def dijkstra(start):
    queue = []
    heappush(queue, (0, start))
    distance = [float('inf') for _ in range(N+1)]
    distance[start] = 0
    
    while queue:
        dist, node = heappop(queue)
        
        if distance[node] < dist:
            continue
        
        for target_node, w in graph[node]:
            cost = distance[node] + w
            if cost < distance[target_node]:
                distance[target_node] = cost
                heappush(queue, (cost, target_node))
    
    return distance

v1, v2 = map(int, readl().split())
one_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

# case 1) 1 -> v1 -> v2 -> N
# case 2) 1 -> v2 -> v1 -> N 중에 최소값

case1 = one_distance[v1] + v1_distance[v2] + v2_distance[N]
case2 = one_distance[v2] + v2_distance[v1] + v1_distance[N]
result = min(case1, case2)
print(result if result < float('inf') else -1)


