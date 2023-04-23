# Дана строка, необходимо посчитать количество слов в строке.

def count_words(my_string):
    words = [word for word in my_string.split()

             if word != "-" and not word.isdigit()]

    return len(words)


result = count_words("Test string 123")
print(result)
