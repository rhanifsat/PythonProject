from operation import *

a = 2
b = 4
c = 6
print('a.', a, '+', b, 'x', c, '-', b)
op1 = kali(b, c)
op2 = jumlah(a, op1)
op3 = kurang(op2, b)
print(' =', a, '+', op1, '-', b)
print(' =', op2, '-', b)
print(' =', op3)