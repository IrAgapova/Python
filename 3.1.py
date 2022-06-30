def my_func():
    try:
     a = float(input("Введите значение 1-ого параметра:"))
     b = float (input("Введите значение 2-ого параметра: "))
    except ValueError:
     return
    func = a // b
    return func
print (my_func())



