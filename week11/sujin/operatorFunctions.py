from keypad2 import numPadList, operatorList, constantList, functionList
import calcFunctions

def numPadOperator(key, display):
    if key == "=":
        try:
            result = str(eval(display))
        except:
            result = 'Error!'
        return result

    elif key == 'C':
        return ''
    else:
        return display + key


def constantOperator(key):
    if key == constantList[0]:
        return '3.141592'
    elif key == constantList[1]:
        return '3E+8'
    elif key == constantList[2]:
        return '340'
    elif key == constantList[3]:
        return '1.5E+8'


def functionOperator(key, display):
    if key == functionList[0]:
        return str(calcFunctions.factorial(display))

    elif key == functionList[1]:
        return str(calcFunctions.decToBin(display))

    elif key == functionList[2]:
        return str(calcFunctions.binToDec(display))

    elif key == functionList[3]:
        return str(calcFunctions.decToRoman(display))
