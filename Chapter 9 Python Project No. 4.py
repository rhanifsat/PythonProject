from random import sample
def randomString(x, n):
    lst = []
    lst[:0] = x
    i = 0
    rdm = []
    while (i < n):
        huruf = (''.join(sample(lst, len(lst))))
        if huruf in lst:
            continue
        else:
            rdm.append(huruf)
            i += 1
    if (i == n):
        print(rdm)

randomString('aku', 5)