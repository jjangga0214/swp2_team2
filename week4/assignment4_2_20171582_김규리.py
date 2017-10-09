#조합을 팩토리얼 함수를 이용해 만듦
def factorial(n):
    if (n <= 1):
        return 1
    return factorial(n - 1) * n


if __name__ == '__main__':
   n = int(input("n :"))
   r = int(input("r :"))

   combination = factorial(n) / (factorial(r) * factorial(n-r))

   print(combination)