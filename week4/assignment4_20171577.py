#팩토리얼을 재귀함수로
def factorial(n):
    if n<= 1:
        return 1
    else:
        return n * factorial(n-1)

print("팩토리얼을 재귀함수로")
n=int(input("n="))
print(factorial(n))


#팩토리얼을 재귀함수로 나타낸걸 이용해 조합 나타내기
def factorial(n):
    if n<= 1:
        return 1
    else:
        return n * factorial(n-1)

print("팩토리얼을 재귀함수로 나타낸걸 이용해 조합 나타내기")
n=int(input("n="))
r=int(input("r="))

result= factorial(n) / (factorial(r) * factorial(n-r))
print(result)



#조합을 재귀함수로
def combination(n,r):
    if n==r or r==0 :
        return 1
    else:
        return combination(n-1,r)+combination(n-1,r-1)

print("조합을 재귀함수로")
n=int(input("n="))
r=int(input("r="))

print(int(combination(n,r)))
