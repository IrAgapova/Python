n =int(input("Введите время в секундах:"))
h = n//3600
n = n % 3600
m = n//60
seconds = n % 60
time = (
    f"{h}:"
    f"{m}:"
    f"{seconds}"
)
print(time)






