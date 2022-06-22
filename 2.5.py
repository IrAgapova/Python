my_list = [7, 5, 3, 3, 2]
n = int(input("Введите число в рейтинг:"))
if n >= 8:
  my_list.insert(0, n)
  print(my_list)
if n == 6:
  my_list.insert(1, n)
  print(my_list)
if n == 7:
  my_list.insert(1, n)
  print(my_list)
if n == 3:
  my_list.insert(4, n)
  print(my_list)
elif n <=2:
 my_list.append(n)
 print(my_list)
else: print("Err!")





