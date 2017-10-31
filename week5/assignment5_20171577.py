import time


#반복적으로 구현한 버전
def iterfibo(n):
	if n<=1:
		return n
	else:
		a=1
		b=1
		c=0
		for i in range(2,n+1):
			a = b
			b = b+c
			c=a
		return b


#재귀적으로 구현한 버전
def fibo(n):
	if n <= 1:
		return n
	return fibo(n - 1) + fibo(n - 2)


while True:
	nbr = int(input("Enter a number: "))
	if nbr == -1:
		break
	ts = time.time()
	fibonumber = iterfibo(nbr)
	ts = time.time() - ts
	print("IterFibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
	ts = time.time()
	fibonumber = fibo(nbr)
	ts = time.time() - ts
	print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
