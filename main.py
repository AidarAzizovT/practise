import pandas
import numpy as np



CORRECT_TITLES = ['ВТП Казани, млн руб.', 'Добавленная стоимость, тыс. руб.',
                  'ДС Обрабатывающие производства, тыс. руб.', 'ДС Строительство, тыс. руб.',
                  'ДС Транспортировка и хранение, тыс. руб.', 'ДС Оптовая и розничная торговля, тыс. руб.',
                  'ДС Деятельность в области информатизации и связи, тыс. руб.']

def is_titles_ok(data_frame_object):
    '''
        >>> df = pandas.read_excel('XXXX')
        >>> is_titles_ok(df)
        ...
    '''
    # + doctest
    titles = data_frame_object["Наименование"].to_list() # определить конкретно, какие параметры отсутствуют
    
    if titles == CORRECT_TITLES:
        return True
    else:
        return False

def is_empty(data_frame_object):
    # + doctest
    foundEmpty = False

    for i in [3, 2, 1]: # использовать генератор списков
        filling = data_frame_object[f"Y-{i}"].to_list() # заменить f"Y-{i}" на года

        for j in range(6):
            if pandas.DataFrame(filling).isnull()[0][j] == True: # yt
                return True

    return False


def check_table(file_name): # переименовать + возвращать bool
    """
    >>> check_table("correct1.xlsx")
    'Everything is fine!'

    >>> check_table("correct2.xlsx")
    'Everything is fine!'

    >>> check_table("wrong1.xlsx")
    'Something is not correct'

    >>> check_table("wrong2.xlsx")
    'Something is not correct'

    >>> check_table("wrong3.xlsx")
    'Something is not correct'

    """
    data_frame_object = pandas.read_excel(file_name)
    if is_titles_ok(data_frame_object) and not is_empty(data_frame_object):
        return 'Everything is fine!'
    else:
        return 'Something is not correct'


#print(check_table("wrong2.xlsx"))




if __name__ == "__main__":
    import doctest
    doctest.testmod()


