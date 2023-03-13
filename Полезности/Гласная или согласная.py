# Программа запрашивает у пользователя букву русского алфавита и выводит информацию
# о ней (гласная, согласная и т.п.)

letter = input('Введите букву русского алфавита: ')
if letter == 'А' or letter == 'а' or letter == 'Е' or letter == 'е' or letter == 'Ё' or\
    letter == 'ё' or letter == 'И' or letter == 'и' or letter == 'О' or letter == 'о' or\
    letter == 'У' or letter == 'у' or letter == 'Ы' or letter == 'ы' or letter == 'Э' or\
    letter == 'э' or letter == 'Ю' or letter == 'ю' or letter == 'Я' or letter == 'я':
    print('гласная')
elif letter == 'Ъ' or letter == 'ъ':
    print('твёрдый знак')
elif letter == 'Ь' or letter == 'ь':
    print('мягкий знак')
else:
    print('согласная')

