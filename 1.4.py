n = int (input ("Введите целое положительное число:"))
max = 0
num_n = n
while num_n > 0:
    digit = num_n % 10
    if digit > max:
        max = digit
        if max == 9:
            break
        num_n // 10
print("Наибольшая цифра в числе {n},равна {max}")
