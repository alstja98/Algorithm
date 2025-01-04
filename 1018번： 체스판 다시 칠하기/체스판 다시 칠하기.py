#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1018                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1018                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 12:21:18 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
readl = sys.stdin.readline
r, c = map(int, readl().split())
map = [list(map(str, readl().strip())) for _ in range(r)]
compare_map1 = [ 
    ['B' if i%2==0 else 'W' for i in range(8)] if j%2==0 
    else ['W' if i%2==0 else 'B' for i in range(8) ] 
    for j in range(8) 
]
compare_map2 = [ 
    ['W' if i%2==0 else 'B' for i in range(8)] if j%2==0 
    else ['B' if i%2==0 else 'W' for i in range(8)] 
    for j in range(8) 
]

end_r = r-8
end_c = c-8
min_count = float('inf')
for start_r in range(end_r+1):
    for start_c in range(end_c+1):
        count1 = 0
        count2 = 0
        for original_r, compare1_r, compare2_r in zip(map[start_r:start_r+8], compare_map1, compare_map2):
            for original_item, compare1_item, compare2_item in zip(original_r[start_c:start_c+8], compare1_r, compare2_r):
                if original_item != compare1_item:
                    count1 += 1
                if original_item != compare2_item:
                    count2 += 1
        min_count = min(min_count, count1, count2)

print(min_count)
        