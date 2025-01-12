#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 24060                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: alstja98 <boj.kr/u/alstja98>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/24060                          #+#        #+#      #+#     #
#    Solved: 2025/01/05 20:33:28 by alstja98      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.setrecursionlimit(10**7)
readl = sys.stdin.readline

N,K=map(int, readl().split())
A = list(map(int, readl().split()))

count = 0
result = -1

def merge_sort(A, p, r): # A[p:r+1]
    global count, result
    if p < r:
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global count, result
    n1 = q-p+1
    n2 = r-q
    L = A[p:q+1]
    R = A[q+1:r+1]
    i,j,k = 0,0,p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
        count += 1
        if count == K:
            print(A[k-1])
            sys.exit()

    while i<n1:
        A[k] = L[i]    
        i+=1
        k+=1
        count += 1
        if count == K:
            print(A[k-1])
            sys.exit()
    
    while j<n2:
        A[k] = R[j]
        j += 1
        k += 1
        count += 1
        if count == K:
            print(A[k-1])
            sys.exit()

merge_sort(A,0,N-1)
print(-1)