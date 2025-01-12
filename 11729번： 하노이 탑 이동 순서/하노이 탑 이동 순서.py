#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11729                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11729                          #+#        #+#      #+#     #
#    Solved: 2025/01/05 19:41:35 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def hanoi(n, start, end, aux, moves):
    if n == 1:
        moves.append((start, end))
        return
    hanoi(n-1, start, aux, end, moves)
    moves.append((start, end))
    hanoi(n-1, aux, end, start, moves)

def main():
    N = int(sys.stdin.readline())
    moves = []
    hanoi(N, 1, 3, 2, moves)
    print(len(moves))
    
    for move in moves:
        print(move[0], move[1])

if __name__ == "__main__":
    main()