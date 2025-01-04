#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 24265                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/24265                          #+#        #+#      #+#     #
#    Solved: 2025/01/04 11:23:58 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def main():
    n = int(sys.stdin.readline().strip())
    execution_count = n * (n - 1) // 2
    time_complexity = 2
    
    print(execution_count)
    print(time_complexity)

if __name__ == "__main__":
    main()