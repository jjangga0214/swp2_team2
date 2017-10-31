import time

def fibo(nbr):
    if nbr <= 1:
        return nbr
    return fibo(nbr - 1) + fibo(nbr - 2)

def iterfibo(nbr):
    number = []
    number.append(0)
    number.append(1)
    for i in range(2, nbr+1):
        number.append(number[i-1]+number[i-2])
    return number[nbr]

while True:
    nbr = int(input("Enter a number : "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
