rus_dic = {"one" : "один", "two" : "два", "three" : "три", "four" : "четыре"}

with open("new_file", "w", encoding="utf-8" ) as r_5:
 with open("text_1", "r", encoding="utf-8") as f_5:
  r_5.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in f_5])