#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1753                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1753                           #+#        #+#      #+#     #
#    Solved: 2025/01/14 20:11:19 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from heapq import heappush, heappop
readl = sys.stdin.readline

V, E = map(int, readl().split())
graph = [[] for _ in range(V+1)]
start_node = int(readl().strip())
distance = [float('inf') for _ in range(V+1)]
for _ in range(E):
    n1, n2, w = map(int, readl().split())
    graph[n1].append((n2, w))

def dijkstra(start):
    queue = []
    heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, node = heappop(queue)
        # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우, 이미 방문한 셈
        if distance[node] < dist:
            continue
        
        for target_node, w in graph[node]:
            cost = distance[node] + w
            if cost < distance[target_node]:
                distance[target_node] = cost
                heappush(queue, (cost, target_node))

dijkstra(start_node)

for index, item in enumerate(distance):
    if index == 0:
        continue
    else:
        if item == float('inf'):
            print('INF')
        else:
            print(item)
    
            





