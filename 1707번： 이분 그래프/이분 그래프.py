#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1707                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1707                           #+#        #+#      #+#     #
#    Solved: 2025/01/12 11:43:51 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.setrecursionlimit(10**6)
readl = sys.stdin.readline
K = int(readl().strip())

def dfs(start_node, graph, node_group):
    result = True
    for target_node in graph[start_node]:
        if target_node not in node_group.keys():
            if node_group[start_node] == 'red':
                node_group[target_node] = 'blue'
            elif node_group[start_node] == 'blue':
                node_group[target_node] = 'red'
            
            result = dfs(target_node, graph, node_group)
        else:
            if node_group[target_node] == node_group[start_node]:
                return False
            
    return result

    
for _ in range(K):
    vlen, elen = map(int, readl().split())
    graph = [[] for _ in range(vlen+1)]
    node_group = {}
    for _ in range(elen):
        n1, n2 = map(int, readl().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    result = True
    for i in range(1, vlen+1):
        if i not in node_group.keys():
            node_group[i] = 'red'
            result = dfs(i, graph, node_group)
            if result == False:
                break
        
    if result:
        print('YES')
    else:
        print('NO')

        