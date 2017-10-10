import time


def fibo(n):
    return fibo(n-1) + fibo(n-2) if n > 1 else n


def iterfibo(n):
    fibo_li = []
    for i in range(n+1):
        if i > 1:
            fibo_li.append(fibo_li[i-1] + fibo_li[i-2])
        else:
            fibo_li.append(i)
    return fibo_li[n]


while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo (%d) = %d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo (%d) = %d, time %.6f" % (nbr, fibonumber, ts))