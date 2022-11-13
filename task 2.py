def get_count_char(str_):  # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower() #нижний регистр
    dict_amount = {}
    for letter in str_:
         alpha = letter.isalpha() #буква или нет
         if alpha == True:
             letter_amount = str_.count(letter)
             dict_amount[letter] = letter_amount
    return dict_amount
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
dict_amount = get_count_char(main_str)
print(get_count_char(main_str))

def get_percent_char(dictionary):

    dict_amount = {}
    values = dictionary.values()
    sum_values = sum(values)
    for key in dictionary:
        dict_amount[key] = dict_amount[key] * 100 / sum_values

    return dict_amount

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_percent_char(dict_amount))
