n_1 = input("Введите название товара:")
v_1 = input("Введите цену товара:")
m = input("Введите количество товара на складе:")
er_1 = input("Введите единицу измерения:")
my_list = [ n_1 ,1]
my_list_2 = [ v_1,1]
my_list_3 = [ m, 1]
my_list_4 = [ er_1, 1]
tuple_1 = (my_list ,)
tuple_2 = (my_list_2 , )
tuple_3 = (my_list_3 ,)
tuple_4 = (my_list_4 ,)
score_dict_1 = dict((x,y)  for x,y in tuple_1)
score_dict_2 = dict( (x,y) for x,y in tuple_2)
score_dict_3 = dict( (x,y) for x,y in tuple_3)
score_dict_4 = dict( (x,y) for x,y in tuple_4)
my_dict = { }
my_dict.update({'название': score_dict_1, "цена" : score_dict_2, "количество": score_dict_3, "единица измерения":score_dict_4})
print(my_dict)





