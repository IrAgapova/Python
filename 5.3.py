with open("famyly_5.3.py", "r", encoding="utf-8") as f_5:
    empl_dict = {line.split()[0] : float(line.split()[1]) for line in f_5}
    print(f'Средняя зарплата = {round(sum(empl_dict.values())/ len (empl_dict) ,2)} \n'
          f'Зарплата меньше 20000 {[e[0] for e in empl_dict.items() if e[1]<20000]}')
