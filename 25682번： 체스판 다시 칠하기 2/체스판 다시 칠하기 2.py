#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25682                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25682                          #+#        #+#      #+#     #
#    Solved: 2025/01/12 20:41:08 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
orig_map = [input().rstrip() for _ in range(N)]

# 두 가지 패턴에 대한 0/1 cost를 누적합으로 구할 배열
w_psum = [[0]*(M+1) for _ in range(N+1)]
b_psum = [[0]*(M+1) for _ in range(N+1)]

# 1) (r + c)가 짝수면 W로 시작하는 체스판일 때는 'W'가 와야 하고,
#    B로 시작하는 체스판일 때는 'B'가 와야 함.
#    (r + c)가 홀수면 반대.
# 2) 해당 칸이 기대값과 다르면 cost = 1, 같으면 cost = 0

for r in range(N):
    w_row_prev = w_psum[r]     # w_psum[r][...]
    w_row_curr = w_psum[r+1]   # w_psum[r+1][...]
    b_row_prev = b_psum[r]
    b_row_curr = b_psum[r+1]
    
    row_str = orig_map[r]
    
    for c in range(M):
        # (r + c)가 짝수일 때 W 패턴은 'W', B 패턴은 'B'가 맞음
        if (r + c) % 2 == 0:
            w_cost = 1 if row_str[c] != 'W' else 0
            b_cost = 1 if row_str[c] != 'B' else 0
        else:
            w_cost = 1 if row_str[c] != 'B' else 0
            b_cost = 1 if row_str[c] != 'W' else 0
        
        # 누적합(PSUM) 공식: psum[r+1][c+1] = 
        #   psum[r][c+1] + psum[r+1][c] - psum[r][c] + cost
        w_row_curr[c+1] = w_row_prev[c+1] + w_row_curr[c] - w_row_prev[c] + w_cost
        b_row_curr[c+1] = b_row_prev[c+1] + b_row_curr[c] - b_row_prev[c] + b_cost

# K x K 범위에서 최소값 찾기
answer = float('inf')

for r in range(K, N+1):
    w_row = w_psum[r]
    b_row = b_psum[r]
    w_row_k = w_psum[r-K]
    b_row_k = b_psum[r-K]
    
    for c in range(K, M+1):
        # sub_sum = psum[r][c] - psum[r-K][c] - psum[r][c-K] + psum[r-K][c-K]
        w_sub_sum = w_row[c] - w_row_k[c] - w_row[c-K] + w_row_k[c-K]
        b_sub_sum = b_row[c] - b_row_k[c] - b_row[c-K] + b_row_k[c-K]
        answer = min(answer, w_sub_sum, b_sub_sum)

print(answer)