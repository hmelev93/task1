def factorial():
    fct = 1
    for i in range(2, num +1):    
        fct *= i
    print(fct)

while True: 
    try:
        num = int(input("Введите число больше 0: "))
        if(num > 1):
            break
        else:
            print('число меньше 0')
    except: 
         print('попробуйте еще раз')

factorial()