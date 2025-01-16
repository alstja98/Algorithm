#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11657                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11657                          #+#        #+#      #+#     #
#    Solved: 2025/01/16 21:40:31 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# import sys
# from collections import deque
# readl = sys.stdin.readline


# N,M = map(int, readl().split())
# graph = [[] for _ in range(N+1)]
# for _ in range(M):
#     A,B,C = map(int, readl().split())
#     graph[A].append((B,C))

# def SPFA(start_node):
#     distance = [float('inf') for _ in range(N+1)]
#     distance[start_node] = 0
#     in_queue = [False for _ in range(N+1)]
#     update_count = [0] * (N + 1)
    
#     queue = deque([start_node])
#     in_queue[start_node] = True

#     while queue:
#         cur_node = queue.popleft()
#         in_queue[cur_node] = False

#         for target_node, dist in graph[cur_node]:
#             if distance[cur_node] != float('inf') and distance[cur_node] + dist < distance[target_node]:
#                 distance[target_node] = distance[cur_node] + dist
#                 update_count[target_node] += 1
                
#                 if update_count[target_node] >= N:
#                     return None
                
#                 if not in_queue[target_node]:
#                     queue.append(target_node)
#                     in_queue[target_node] = True
    
#         # --- 음수 사이클 추가 체크 (벨만포드 5단계 유사) ---
#     for u in range(1, N+1):
#         # 시작점에서 도달 불가능하면 패스
#         if distance[u] == float('inf'):
#             continue
#         for v, cost in graph[u]:
#             if distance[u] + cost < distance[v]:
#                 # 음수 사이클 발견
#                 return None

#     return distance


# dist = SPFA(1)
# if dist is None:
#     print(-1)
# else:
#     for i in range(2, N+1):
#         if dist[i] == float('inf'):
#             print(-1)
#         else:
#             print(dist[i])
    
    
import sys
readl = sys.stdin.readline

N, M = map(int, readl().split())
edges = []  # (시작노드, 도착노드, 가중치) 형태로 간선 저장

for _ in range(M):
    A, B, C = map(int, readl().split())
    edges.append((A, B, C))

def bellman_ford(start):
    # 거리 배열: 시작 노드는 0, 나머지는 무한대
    distance = [float('inf')] * (N+1)
    distance[start] = 0

    # 1. 최대 (N-1)번 반복하며 모든 간선을 확인 & 거리 갱신
    for _ in range(N-1):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # 2. 추가 1번 확인(음수 사이클 체크)
    #    만약 여기서도 갱신이 일어난다면, "시작점에서 도달 가능한 음수 사이클" 존재
    for u, v, w in edges:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            return None  # 음수 사이클 존재

    return distance

dist = bellman_ford(1)

# dist가 None이면 => 시작점(1번)으로부터 도달 가능한 음수 사이클 있음 => -1 출력
if dist is None:
    print(-1)
else:
    # 2번 노드부터 N번 노드까지 최단 거리 출력
    # 도달 불가능한 경우엔 -1 출력
    for i in range(2, N+1):
        if dist[i] == float('inf'):
            print(-1)
        else:
            print(dist[i])