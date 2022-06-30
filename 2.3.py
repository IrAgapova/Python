n = int(input("Введите номер месяца:"))
my_list = [1, 2, 12, 3, 4, 5, 6, 7, 8, 9, 10, 11]
if n in my_list[0:3]: print ("зима")
if n in my_list[3:6]: print ("весна")
if n in my_list[6:9]: print("лето")
if n in my_list[9:13]: print ("осень")