import sys


def factorial(n):
    if n < 0:
        raise ValueError("the argument of factorial have to be integer 0 or positive. ")
    return 1 if n == 0 else n * factorial(n - 1)


def combination(n, r=-1, **keyword):
    if isinstance(n, tuple):
        try:
            n, r = n[0], n[1]
        except IndexError:
            raise ValueError("combination needs 2 args")
    result = 1

    if not (0 <= r <= n):
        raise ValueError("the 'r' of combination have to be 0 <= integer <= 'n'. ")
    elif r == 0 or r == n:
        pass
    elif keyword.get("recursive", False):
        result = combination(n - 1, r, recursive=True) + combination(n - 1, r - 1, recursive=True)
    else:
        result = factorial(n) / (factorial(r) * factorial(n - r))
    return int(result)


def demo(parse, terminate, cal, show):
    while True:
        n = input("Enter a number : ").strip()
        try:
            n = parse(n)
            if terminate(n) == -1:
                print('bye')
                break
            result = cal(n)
        except ValueError as e:
            print(e)
            continue
        print(show(n, result))


if __name__ == "__main__":
    sys.setrecursionlimit(999999999)

    while True:
        response = input("Factorial 계산은 f, Combination 계산은 c를 입력해 주세요. [f/c] : ").strip()
        if response == "f":
            demo(int, lambda n: n, factorial, lambda arg, result: "%d!  =  %d" % (arg, result))
            break
        elif response == "c":
            demo(lambda s: tuple(map(int, s.split())), lambda n: n[0], combination,
                 lambda arg, result: "%dC%d  =  %d" % (arg[0], arg[1], result))
            break
        else:
            print("f 또는 c중 하나를 입력해 주세요")
