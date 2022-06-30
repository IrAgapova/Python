from sys import (argv)
name,measure, wish, premium = argv
print("Выработка в часах:", measure)
print("Ставка:", wish)
print("Премия:", premium)
print ("Зарплата:", int(measure)*int(wish)+int(premium) )
