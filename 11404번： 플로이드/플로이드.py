#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11404                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11404                          #+#        #+#      #+#     #
#    Solved: 2025/01/14 21:49:34 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from heapq import heappush, heappop
readl = sys.stdin.readline

city_len = int(readl().strip())
bus_len = int(readl().strip())
graph = [[] for _ in range(city_len + 1)]

for _ in range(bus_len):
    sc, tc, cost = map(int, readl().split())
    graph[sc].append((tc, cost))

def dijkstra(start):
    distance = [float('inf') for _ in range(city_len + 1)]
    distance[start] = 0
    queue = []
    heappush(queue, (0, start))
    
    while queue:
        dist, cur_node = heappop(queue)
        
        if distance[cur_node] < dist:
            continue

        for target_node, w in graph[cur_node]:
            new_cost = dist + w
            if distance[target_node] > new_cost:
                distance[target_node] = new_cost
                heappush(queue, (new_cost, target_node))
    
    return distance

ans_list = [[float('inf')]*city_len for _ in range(city_len)]

for r_index, row in enumerate(ans_list):
    r_distance = dijkstra(r_index+1)
    for c_index, col in enumerate(row):
        if r_index == c_index:
            ans_list[r_index][c_index] = 0
            continue
        else:
            ans_list[r_index][c_index] = r_distance[c_index+1]
            

for row in ans_list:
    for c_index, val in enumerate(row):
        if val == float('inf'):
            row[c_index] = 0   # 도달 불가능할 때는 0으로 설정
    print(*row)
    
