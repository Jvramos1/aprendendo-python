A,B,C = input().split()

A = int(A)
B = int(B)
C = int(C)



abs = A - B

if abs < 0 : 
    abs = abs * (-1)


maior = (A + B + abs) / 2
abs = maior - C 

if abs < 0 :
    abs = abs * (-1)

maior = (maior + C + abs) / 2


print(int(maior))

