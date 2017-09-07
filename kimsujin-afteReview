#factorial function
#Input : n
#Output : n!

def factorial(n):

    if n == 0:
        return 1

    else:
        result = 1
        while n >0:
            result *= n
            n -= 1
        return result

#Main Program

while True:

    try:

        n = int(input('Enter a number : '))
        if n == -1:
            break
        elif n < 0:
            print('0 또는 양의 정수를 입력해주세요.')
        else:
            print(n, "! = ", factorial(n))

    except:

        print('0 또는 양의 정수를 입력해주세요.')
        
