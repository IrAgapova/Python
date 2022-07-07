my_dict = {}
with open("pr_1", "r", encoding="utf-8") as dict_1:
    for line in dict_1:
        name, stats = line.split(":")
        name_sum = sum(map(int,"".join([i for i in stats if i == ' ' or "9" >= i >= "0"]).split()))
        my_dict[name] = name_sum
    print(f'{my_dict}')

