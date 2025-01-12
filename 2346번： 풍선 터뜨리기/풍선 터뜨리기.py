#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2346                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2346                           #+#        #+#      #+#     #
#    Solved: 2025/01/05 18:21:25 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# deque 에서 rotate() 를 이용하면 쉽게 풀 수 있다!
from collections import deque

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    balloon_numbers = list(map(int, input().split()))
    
    balloons = deque([(i+1, num) for i, num in enumerate(balloon_numbers)])
    
    pop_order = []
    while balloons:
        current_balloon = balloons.popleft()
        pop_order.append(current_balloon[0]) 
        
        if not balloons:
            break 
        
        move = current_balloon[1]
        if move > 0:
            balloons.rotate(-(move - 1))
        else:
            balloons.rotate(-move)
    
    print(' '.join(map(str, pop_order)))

if __name__ == "__main__":
    main()