# factirial
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


num = int(input('num : '))
print(num, "! =", factorial(num))


# combination factorial
def combi_fac(n, r):
    if n < r:
        return 'n은 r이상'
    elif n == r:
        return 1
    else:
        if n == r:
            return 1
        if n == 0:
            return 'n은 1이상의 정수여야 합니다.'
        else:
            if r < 0:
                return 'r은 0이상의 정수여야 합니다.'
            elif r == 0:
                return 1
            else:
                return factorial(n) // factorial(r) // factorial(n - r)

n = int(input('n: '))
r = int(input('r: '))
print(combi_fac(n, r))


# combination recursive
def combi_recur(n, r):
    if n < r:
        return 'n은 r이상'
    elif n == r:
        return 1
    else:
        if n == 0:
            return 'n은 1이상의 정수여야 합니다.'
        else:
            if r < 0:
                return 'r은 0이상의 정수여야 합니다.'
            elif r == 0:
                return 1
            else:
                return combi_recur(n - 1, r - 1) + combi_recur(n - 1, r)

n = int(input('n: '))
r = int(input('r: '))
print(combi_recur(n, r))