#팩토리얼을 재귀함수로 만들기
def factorial(n):
    if (n <= 1):
        return 1
    return factorial(n - 1) * n

n = int(input("n : "))
print(factorial(n))