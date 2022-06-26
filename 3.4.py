def my_func():
    """Возведение x в степень y"""
    x = float(input("Введите положительное число х:"))
    if x >= 0: print(x)
    else:
     print("Wrong! Try again!")
    y = float(input("Введите отрицательное число y:"))
    if y <= 0: print(y)
    else:
     print("Wrong! Try again!")
    return ( x ** y  )
print(my_func())


