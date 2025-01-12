#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 24445                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/24445                          #+#        #+#      #+#     #
#    Solved: 2025/01/12 17:02:13 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
readl = sys.stdin.readline
N,M,R = map(int, readl().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 =  map(int, readl().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
for row in graph:
    row.sort(reverse=True)

visited = [False for _ in range(N+1)]
visited[R] = True
node_dict = {i:0 for i in range(1,N+1)}
queue = deque([R]) #노드번호, 방문 순서
order = 0

while queue:
    cur_node = queue.popleft()
    order += 1
    node_dict[cur_node] = order
    
    for target_node in graph[cur_node]:
        if visited[target_node] == False:
            visited[target_node] = True
            queue.append(target_node)

for i in range(1,N+1):
    print(node_dict[i])