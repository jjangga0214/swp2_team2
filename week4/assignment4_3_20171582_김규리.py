def factorial(n):
    if (n <= 1):
        return 1
    return factorial(n - 1) * n

def combination_1(n, r):
    com1 = factorial(n) / (factorial(r) * factorial(n - r))
    return com1

def combination_2(n, r):
    if n <= 1 and r <= 1:
        return 1
    com2 = combination_1(n-1, r-1) + combination_1(n-1, r)
    return com2

if __name__ == '__main__':
   n = int(input("n :"))
   r = int(input("r :"))

   print(combination_2(n, r))