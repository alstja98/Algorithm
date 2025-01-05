#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17103                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17103                          #+#        #+#      #+#     #
#    Solved: 2025/01/05 15:15:55 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# import sys
# import math
# readl = sys.stdin.readline

# def is_prime_number(num):
#     if num < 2 :
#         return 0
#     for i in range(2, int(math.sqrt(num))+1):
#         if num % i == 0:
#             return 0
        
#     return 1

# tc = int(readl().strip())
# N = [ int(readl().strip()) for _ in range(tc)]
# primes = [ True if is_prime_number(num) else False for num in range(max(N)+1) ]
# for n in N:
#     count = 0
#     for p in range(2, n//2 + 1):
#         if primes[p] and primes[n - p]:
#             count += 1

#     print(count)

import sys
import math

input = sys.stdin.readline

def sieve(max_limit):
    sieve = [True] * (max_limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(max_limit)) + 1):
        if sieve[i]:
            for j in range(i * i, max_limit + 1, i):
                sieve[j] = False
    return sieve

def main():
    t = int(input())
    Ns = [int(input()) for _ in range(t)]
    maxN = max(Ns)

    # 1) 에라토스테네스의 체로 0 ~ maxN까지 소수판별
    prime_sieve = sieve(maxN)

    # 2) 실제 소수들만 리스트로 저장
    prime_list = [i for i in range(2, maxN+1) if prime_sieve[i]]
    
    # 3) 각 테스트 케이스 처리
    for n in Ns:
        count = 0
        # p가 n//2 이하인 소수에 대해서만 확인
        for p in prime_list:
            if p > n // 2:
                break
            if prime_sieve[n - p]:
                count += 1
        print(count)

if __name__ == "__main__":
    main()