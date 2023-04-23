# Дана строка, необходимо «перевернуть» все слова в строке, записав их «задом наперёд».
# Порядок слов должен остаться прежним, знаки препинания (точка, запятая, восклицательный знак)
# тоже должны остаться на своих местах.


def reverse_words(my_string):
    words = my_string.split()

    results = []

    for word in words:

        new_word = word[::-1]

        if '.' in word[-1] or ',' in word[-1] or '!' in word[-1]:
            new_word = word[:-1:-1] + word[-1]

        results.append(new_word)

    return ' '.join(results)


print(reverse_words("Don't worry, be happy!"))
