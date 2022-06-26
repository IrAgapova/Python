def int_func():
    """"Введите строку из латинских символов"""
    a = input("Введите строку из латинских символов:")
    for word in a.split():
        chars = 0
        for char in word:
            if 97<= ord(char) <= 122:
                chars += 1
                print(word.title()) if chars == len(word) else f"{word} - только маленькие английские буквы!"
print (int_func())

