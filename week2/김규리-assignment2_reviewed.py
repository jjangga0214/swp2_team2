n = int()

def factorial(a):
    result = 1
    for i in range(1, a+1):
        result *= i
    if a >= 0:
        return result
    else:
        return


while True:
    n = int(input("Enter a number:"))
    if n >= 0:
        print(factorial(n))
    elif n < -1:
        print("0과 양의 정수만 입력하시오.")
    else:
        break
