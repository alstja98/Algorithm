#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1193                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1193                           #+#        #+#      #+#     #
#    Solved: 2025/01/02 21:10:22 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import math

def find_fraction(X):
    # 1. 층(k) 찾기: k(k+1)/2 >= X가 되는 최소 k
    k = int(math.sqrt(2*X))  # 근사값으로 초기화
    while (k*(k+1))//2 < X:
        k += 1

    # 2. 층 내에서 몇 번째 위치(p)인지 계산
    total_prev = (k-1)*k//2
    p = X - total_prev

    # 3. 홀수/짝수 층에 따라 분자/분모 계산 (수정된 부분)
    if k % 2 == 1:
        # 홀수 층: 분자가 큰 값부터 시작
        numerator = k + 1 - p
        denominator = p
    else:
        # 짝수 층: 분자가 작은 값부터 시작
        numerator = p
        denominator = k + 1 - p

    return f"{numerator}/{denominator}"

def main():
    X = int(sys.stdin.readline())
    print(find_fraction(X))

if __name__ == "__main__":
    main()