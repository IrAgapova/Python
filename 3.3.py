def my_func ():
    """Сумма наибольших аргументов"""
    a = float (input("Введите значение аргумента 1:"))
    b = float (input("Введите значение аргумента 2:"))
    c = float (input("Введите значение аргумента 3:"))
    g = (a+b,b+c,a+c)
    print(max(g))
print(my_func())

