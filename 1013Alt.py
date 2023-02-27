A,B,C = input().split()

A = int(A)
B = int(B)
C = int(C)

if A > B:
    if A > C:
        print('{} eh o maior'.format(A))
    else:
        print('{} eh o maior'.format(C))
else:
    if B > C:
        print('{} eh o maior'.format(B))
    else:
        print('{} eh o maior'.format(C))


