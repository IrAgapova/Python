def person_life ():
    """вводим данные пользователя"""
    name = input("Введите свое имя:")
    surname = input("Введите свою фамилию:")
    a = int(input("Введите год рождения:"))
    b = input("Город проживания:")
    m = input("e-mail:")
    d = int (input("Номер телефона:"))
    g = (f" Имя : {name}, Фамилия : {surname}, Год рождения :{a}, Город проживания :{b},e-mail-{m},Номер телефона:{d}")
    return (g)
print(person_life())