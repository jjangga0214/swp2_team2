n = input("Enter a number: ")


while True:
    try:
        num = int(n)
        if num == -1:
            break
        elif num > -1:
            result = 1
            for i in range(1, num + 1):
                result *= i
            print("%d! = %d" %(num,result))
            n = input("Enter a number: ")
        else:
            n = input("Enter a number: ")
    except:
        n = input("Enter a number: ")