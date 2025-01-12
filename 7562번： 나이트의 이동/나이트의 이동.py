#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7562                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7562                           #+#        #+#      #+#     #
#    Solved: 2025/01/12 17:46:24 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque

def knight_moves(l, start, target):
    directions = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)
    ]
    
    visited = [[False] * l for _ in range(l)]
    
    queue = deque([(start[0], start[1], 0)])  # (x, y, 이동 횟수)
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, moves = queue.popleft()
        
        if (x, y) == target:
            return moves
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))
    
    return -1

if __name__ == "__main__":
    T = int(input()) 
    
    for _ in range(T):
        l = int(input()) 
        start = tuple(map(int, input().split()))  # 시작 위치
        target = tuple(map(int, input().split()))  # 목표 위치
        
        print(knight_moves(l, start, target))