num = int(input("Введите номер месяца:"))
n = 1,2,12
v = 3,4,5
m = 6,7,8
c = 9,10,11
my_dict = { n:"зима", v: "весна", m:"лето", c:"зима"}
if num in n: print(my_dict.get(n))
if num in v: print(my_dict.get(v))
if num in m: print(my_dict.get(m))
if num in c: print(my_dict.get(c))

