def power_modulo(A,B,C):
    if B==0:
        return 1
    if B==1:
        return B
    P=power_modulo(A,B//2,C)
    
    if B%2==0:
        return (P*P)%C
    else:
        return (P*P*A)%C


A,B,C=map(int,input().split())
print(power_modulo(A,B,C))

"""
Input 1:
A = 2
B = 3
C = 3
Output 1:
2


Input 2:
A = 3
B = 3
C = 1
Output 2:
0
"""

