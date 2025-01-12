#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 24480	                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/24480	                         #+#        #+#      #+#     #
#    Solved: 2025/01/11 20:46:48 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.setrecursionlimit(10**6)
readl = sys.stdin.readline
N,M,R = map(int, readl().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

# 그래프 생성
for _ in range(M):
    n1, n2 = map(int, readl().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 각 노드 연결된 노드 오름차순 정렬
for node_list in graph:
    node_list.sort(reverse=True)

node_dict = { i:0 for i in range(1, N+1)}
order = 1
def dfs(start_node):
    global order
    visited[start_node] = True
    node_dict[start_node] = order
    order += 1

    for target_node in graph[start_node]:
        if visited[target_node] == False:
            dfs(target_node)
    
    
dfs(R)
for i in range(1, N+1):
    print(node_dict[i])
    