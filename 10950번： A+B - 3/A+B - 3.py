#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10950                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10950                          #+#        #+#      #+#     #
#    Solved: 2025/01/01 12:45:14 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

def main():
    # 빠른 입력을 위해 sys.stdin 사용
    input = sys.stdin.readline
    
    # 첫 번째 줄에서 테스트 케이스의 개수 T 입력
    T = int(input())
    
    for _ in range(T):
        # 각 테스트 케이스마다 A와 B를 입력받아 리스트로 저장
        A, B = map(int, input().split())
        # A + B를 출력
        print(A + B)

if __name__ == "__main__":
    main()