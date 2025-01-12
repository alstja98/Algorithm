#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14889                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14889                          #+#        #+#      #+#     #
#    Solved: 2025/01/09 22:58:35 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from itertools import permutations, combinations

readl = sys.stdin.readline

N = int(readl().strip())
s_map = [ list(map(int,readl().split())) for _ in range(N) ]
abil_dict = {}

all_member = set([i for i in range(1,N+1)])
start_team_comb = combinations(all_member, int(N//2))

def cal_ability(team):
    perm = permutations(team, 2)
    ret = 0
    for i, j in perm:
        ret += s_map[i-1][j-1]
    
    return ret
    

ans = float('inf')
for start_team in start_team_comb:
    start_team = set(start_team)
    link_team = all_member - start_team
    tup_start_team = tuple(start_team)
    tup_link_team = tuple(link_team)
    if tup_start_team not in abil_dict.keys():
        start_abil = cal_ability(start_team)
        abil_dict[tup_start_team] = start_abil
    else:
        start_abil = abil_dict[tup_start_team]
        
    if tup_link_team not in abil_dict.keys():
        link_abil = cal_ability(link_team)
        abil_dict[tup_link_team] = link_abil
    else:
        link_abil = abil_dict[tup_link_team]
    
    ans = min(ans, abs(start_abil - link_abil))

print(ans)
