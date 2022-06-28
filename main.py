import pandas
import numpy as np



CORRECT_TITLES = ['ВТП Казани, млн руб.', 'Добавленная стоимость, тыс. руб.',
                  'ДС Обрабатывающие производства, тыс. руб.', 'ДС Строительство, тыс. руб.',
                  'ДС Транспортировка и хранение, тыс. руб.', 'ДС Оптовая и розничная торговля, тыс. руб.',
                  'ДС Деятельность в области информатизации и связи, тыс. руб.']

def is_titles_ok(data_frame_object):
    '''
     + doctest
    определить конкретно, какие параметры отсутствуют

        >>> df = pandas.read_excel('wrong1.xlsx')
        >>> is_titles_ok(df)
        С параметром на 7 строке ошибка
        False

        >>> df = pandas.read_excel('wrong3.xlsx')
        >>> is_titles_ok(df)
        С параметром на 4 строке ошибка
        False

        >>> df = pandas.read_excel('correct1.xlsx')
        >>> is_titles_ok(df)
        True

         >>> df = pandas.read_excel('correct2.xlsx')
        >>> is_titles_ok(df)
        True


    '''
    foundMistake = False
    counter = 2 #Параметры начинаются со 2 строчке в excel
    for title in data_frame_object.values:
        if title[0] not in CORRECT_TITLES:
            print(f'С параметром на {counter} строке ошибка')
            foundMistake = True
        counter += 1

    if foundMistake == False:
        return True
    else:
        return False



def is_empty(data_frame_object):
    # + doctest
    # просто пройтись по всем 3м столбцам начиная со второго
    # заменить f"Y-{i}" на года

    '''
        >>> df = pandas.read_excel('wrong2.xlsx')
        >>> is_empty(df)
        Ошибка по  4 столбцу 4 строке
        Ошибка по  3 столбцу 6 строке
        Ошибка по  2 столбцу 7 строке
        True

        >>> df = pandas.read_excel('wrong3.xlsx')
        >>> is_empty(df)
        Ошибка по  4 столбцу 8 строке
        True

        >>> df = pandas.read_excel('correct1.xlsx')
        >>> is_empty(df)
        False
    '''

    foundEmpty = False
    line = 2
    row = 2

    for string in data_frame_object.values:
        for element in string[1:]:
            if pandas.isna(element):
                foundEmpty = True
                print(f"Ошибка по  {str(row)} столбцу {str(line)} строке")
            row += 1
        row = 2
        line += 1

    if foundEmpty == True:
        return True
    else:
        return False






def is_everything_ok(file_name): # переименовать + возвращать bool
    '''
        >>> is_everything_ok("correct1.xlsx")
        True

        >>> is_everything_ok("wrong1.xlsx")
        С параметром на 7 строке ошибка
        False

        >>> is_everything_ok("wrong2.xlsx")
        Ошибка по  4 столбцу 4 строке
        Ошибка по  3 столбцу 6 строке
        Ошибка по  2 столбцу 7 строке
        False

    '''

    data_frame_object = pandas.read_excel(file_name)
    if is_titles_ok(data_frame_object) and not is_empty(data_frame_object):
        return True
    else:
        return False




if __name__ == "__main__":
    import doctest
    doctest.testmod()





