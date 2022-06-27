import pandas
import numpy as np



CORRECT_TITLES = ['ВТП Казани, млн руб.', 'Добавленная стоимость, тыс. руб.',
                  'ДС Обрабатывающие производства, тыс. руб.', 'ДС Строительство, тыс. руб.',
                  'ДС Транспортировка и хранение, тыс. руб.', 'ДС Оптовая и розничная торговля, тыс. руб.',
                  'ДС Деятельность в области информатизации и связи, тыс. руб.']

def is_titles_ok(data_frame_object):
    titles = data_frame_object["Наименование"].to_list()
    if titles == CORRECT_TITLES:
        return True
    else:
        return False

def is_empty(data_frame_object):

    foundEmpty = False
    for i in [3, 2, 1]:
        filling = data_frame_object[f"Y-{i}"].to_list()
        for j in range(6):
            if pandas.DataFrame(filling).isnull()[0][j] == True:
                return True
    return False


def check_table(file_name):
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


