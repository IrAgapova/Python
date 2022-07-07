with open( "text_1.py", 'r',encoding="utf-8") as f_tex:
    my_line = f_tex.readline()
    for index, value in enumerate(f_tex, 1) :
        num_w = len(value.split( ))
        print(f'Строка {index} содержит {num_w} слов ')






