#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1735                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1735                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 17:52:41 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import math

def add_fractions(A, B, C, D):
    # 분수의 합 계산
    numerator = A * D + B * C
    denominator = B * D
    
    # 최대공약수 계산
    gcd = math.gcd(numerator, denominator)
    
    # 기약분수로 만들기
    reduced_numerator = numerator // gcd
    reduced_denominator = denominator // gcd
    
    return reduced_numerator, reduced_denominator

def main():
    # 입력 받기
    A, B = map(int, sys.stdin.readline().split())
    C, D = map(int, sys.stdin.readline().split())
    
    # 분수 더하기
    result_num, result_den = add_fractions(A, B, C, D)
    
    # 결과 출력
    print(result_num, result_den)

if __name__ == "__main__":
    main()