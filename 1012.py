A,B,C = input().split()

A = float(A)
B = float(B)
C = float(C)

pi = 3.14159


tr = A * C / 2
print("TRIANGULO: %.3f" % tr)
ac = pi * C * C
print("CIRCULO: %.3f" % ac)
at = (A + B) * C / 2
print("TRAPEZIO: %.3f" % at)
aq = B * B 
print("QUADRADO: %.3f" % aq)
ar = A * B
print("RETANGULO: %.3f" % ar)

