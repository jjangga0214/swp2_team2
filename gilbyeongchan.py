# author : jjangga 17280214 길병찬
import functools


def factorial(n):
    return 1 if n == 0 \
        else functools.reduce(lambda former, latter:
                              former * latter, range(1, n + 1))

while True:
    n = input("An argument for factorial : ")

    try:
        # 문자열이나 소수 입력시 Exception 이 발생하여 다시 input 을 받는다.
        int_n = int(n)

        # -1 미만의 정수 입력시 다시 input을 받는다.
        if int_n < -1:
            raise ValueError()

        # -1 입력시 종료한다.
        elif int_n == -1:
            break

        print(factorial(int_n))

    except ValueError:
        print("Invalid Argument. Please input again")

print("Terminated")
