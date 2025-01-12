#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4779                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4779                           #+#        #+#      #+#     #
#    Solved: 2025/01/05 19:42:51 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def generate_cantor(n):
    length = 3 ** n
    pattern = ['-'] * length

    def remove_middle(start, length):
        if length < 1:
            return
        mid_start = start + length // 3
        mid_end = start + 2 * length // 3
        for i in range(mid_start, mid_end):
            pattern[i] = ' '
        remove_middle(start, length // 3)
        remove_middle(start + 2 * (length // 3), length // 3)

    remove_middle(0, length)
    return ''.join(pattern)

def main():
    input = sys.stdin.read().split()
    for line in input:
        if line.strip() == '':
            continue
        n = int(line)
        cantor_set = generate_cantor(n)
        print(cantor_set)

if __name__ == "__main__":
    main()