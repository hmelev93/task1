import math
def factorial(num):
    return math.factorial(int(num))


while True: 
    try:
        num = int(input("Введите число больше 0: "))
        if(num > 1):
            print(factorial(num))
            break
        else:
            print('число меньше 0')
    except: 
        print('попробуйте еще раз')