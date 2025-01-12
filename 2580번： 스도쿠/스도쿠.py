#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2580                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2580                           #+#        #+#      #+#     #
#    Solved: 2025/01/11 13:50:36 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from itertools import permutations
readl = sys.stdin.readline

sudoku = [list(map(int, readl().split())) for _ in range(9)]
comp_set = set([i for i in range(1,10)])

# 각 행에서 빈칸이 하나인 곳 채워넣기
for row in sudoku:
    row_set = set(row)
    remain_set = comp_set - row_set
    if len(remain_set) == 1:
        for i in range(9):
            if row[i] == 0:
                row[i] = list(remain_set)[0]

# 각 열에서 빈칸이 하나인 곳 채워넣기
for c_index, col in enumerate(zip(*sudoku)):
    col_set = set(col)
    remain_set = comp_set - col_set
    if len(remain_set) == 1:
        for i in range(9):
            if col[i] == 0:
                sudoku[i][c_index] = list(remain_set)[0]
                
# 남은 빈칸 위치 찾기
blanks = []
for r in range(9):
    for c in range(9):
        if sudoku[r][c] == 0:
            blanks.append((r,c))

def is_safe(row, col, target):
    # 행 체크
    if target in sudoku[row]:
        return False
    
    # 열 체크
    for r in range(9):
        if sudoku[r][col] == target:
            return False
    
    # 3*3 박스 체크
    box_row_start = (row//3) * 3
    box_col_start = (col//3) * 3
    for r in range(box_row_start, box_row_start+3):
        for c in range(box_col_start, box_col_start+3):
            if sudoku[r][c] == target:
                return False
    return True
        
                
# 빈칸인 곳 채워넣기 - 백트래킹
def backtraking(idx):
    if idx == len(blanks):
        return True
    
    r,c = blanks[idx]
    for num in range(1,10):
        if is_safe(r,c,num):
            sudoku[r][c] = num
            if backtraking(idx+1):
                return True
            sudoku[r][c] = 0
    
    return False
            

backtraking(0)
for row in sudoku:
    print(*row)