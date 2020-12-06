myData = ['apel', 'rambutan', 'jeruk',]

def sortStringByChar(lst):
    lst.sort(key = len, reverse = True)
    print(lst)

sortStringByChar(myData)