def sum_num( ):
    s = 0
    while True:
        err = "False"
        str_1 = input("Введите числа:").split()
        for num in str_1:
            if num.lower () == "q":
                return s
            else:
                try:
                    s+=int(num)
                except ValueError:
                    err = True
        if err:
            print("Неверный набор!")
        print(f"Сумма чисел = {s}")
print(sum_num())





