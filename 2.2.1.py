my_list = input("Введите числа списка в строку;")
print("Список:")
idx = len(my_list) if len(my_list)%2 == len(my_list) - 1
my_list[:idx:2],my_list[1:idx:2]= my_list[1:idx:2], my_list[:idx:2]
print("Список-2:", my_list)


