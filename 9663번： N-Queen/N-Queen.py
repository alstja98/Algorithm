#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9663                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9663                           #+#        #+#      #+#     #
#    Solved: 2025/01/11 12:38:12 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

readl = sys.stdin.readline
N = int(readl().strip())
ans = 0

# def is_safe(row, col, queens):
#     for r,c in queens:
#         if c == col or abs(r-row) == abs(c-col):
#             return False
#     return True

# def backtraking(cur_row, queens):
#     global ans
    
#     if cur_row == N:
#         ans += 1
#         return
        
#     for col in range(N):
#         if is_safe(cur_row, col, queens):
#             queens.append((cur_row, col))
#             backtraking(cur_row+1, queens)
#             queens.pop()
            
def backtrack(row, cols, diag1, diag2):
    global ans
    if row == N:
        ans += 1
        return
    
    for col in range(N):
        if col in cols or (row+col) in diag1 or (row-col) in diag2:
            continue

        cols.add(col)
        diag1.add(row+col)
        diag2.add(row-col)
        backtrack(row+1, cols, diag1, diag2)
        cols.remove(col)
        diag1.remove(row+col)
        diag2.remove(row-col)

# backtraking(0, [])
backtrack(0, set(), set(), set())
print(ans)