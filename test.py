import sys
from queue import deque

def dfs(graph, start, visited):
    visit_order = [start]
    visited[start] = True

    for search_node in graph[start]:
        if visited[search_node] == False:
            visit_order += dfs(graph, search_node, visited)

    return visit_order

# 정점의 수 N, 간선 개수 M, 탐색 시작할 정점 번호 V
N, M, V = list(map(int, sys.stdin.readline().split()))

# 간선 정보
edge_list = []
for _ in range(M):
    node1, node2 = list(map(int, sys.stdin.readline().split()))
    edge_list.append((node1, node2))

# 그래프 생성
graph = [[] for _ in range(N+1)]
for node1, node2 in edge_list:
    graph[node1].append(node2)
    graph[node2].append(node1)

# 그래프의 정점 순서 정렬
for ele in graph:
    ele.sort()

# dfs 탐색
visited = [ False for _ in range(N+1) ]
dfs_list = dfs(graph, V, visited)

# bfs 탐색 전, visited 초기화
visited = [ False for _ in range(N+1) ]
visited[V] = True
queue = deque([V])
bfs_list = [V]

# bfs 탐색 시작
while queue:
    start_node = queue.popleft()

    for search_node in graph[start_node]:
        if visited[search_node] == False:
            visited[search_node] = True
            queue.append(search_node)
            bfs_list.append(search_node)
        
print(' '.join(map(str, dfs_list)))
print(' '.join(map(str, bfs_list)))
