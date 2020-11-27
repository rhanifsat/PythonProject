from operation import *

a = 10
b = 2
c = 7
d = 5
e = 12
f = 34
print('c. (', a, '+', b, ') / (', c, '+', d, ') / (', e, '-', f, ')')
op1 = jumlah(a, b)
op2 = jumlah(c, d)
op3 = kurang(e, f)
op4 = op1/op2
op5 = op4/op3
print('  =   ', op1, '    /   ', op2, '    /    ', op3)
print('  =         ', op4, '         /    ', op3)
print('  =', op5)
