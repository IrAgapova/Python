from random import randint
with open("Num_5", "w", encoding="utf-8") as n_5:
    my_list = [randint(1, 100) for _ in range(100)]
    n_5.write(" ".join(map(str, my_list)))
print(f'Сумма элементов - {sum(my_list)}')
