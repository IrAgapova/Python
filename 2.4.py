my_str = (input("Введите цитату:")).split()
for i , word in enumerate (my_str, 1) :
        print( f'{i}  {word[:10]}')


