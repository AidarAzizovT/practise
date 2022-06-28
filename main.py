import pandas

CORRECT_TITLES = ['ВТП Казани, млн руб.', 'Добавленная стоимость, тыс. руб.',
                  'ДС Обрабатывающие производства, тыс. руб.', 'ДС Строительство, тыс. руб.',
                  'ДС Транспортировка и хранение, тыс. руб.', 'ДС Оптовая и розничная торговля, тыс. руб.',
                  'ДС Деятельность в области информатизации и связи, тыс. руб.']


def is_titles_ok(data_frame_object: pandas.DataFrame) -> bool:
    '''
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
    counter = 2  # Параметры начинаются со 2 строчке в excel
    for index_tt, title in enumerate(data_frame_object.values):
        if title[0] not in CORRECT_TITLES:
            print(f'С параметром на {index_tt + 2} строке ошибка')
            foundMistake = True
    return not foundMistake


def is_empty(data_frame_object: pandas.DataFrame) -> bool:
    '''
        >>> df = pandas.read_excel('correct1.xlsx')
        >>> is_empty(df)
        False

        >>> df = pandas.read_excel('wrong1.xlsx')
        >>> is_empty(df)
        Ошибка в значении  ДС Транспортировка и хранение, тыс. руб. за  Y-3 год
        Ошибка в значении  ДС Транспортировка и хранение, тыс. руб. за  Y-2 год
        True

        >>> df = pandas.read_excel('wrong2.xlsx')
        >>> is_empty(df)
        Ошибка в значении  ДС Обрабатывающие производства, тыс. руб. за  Y-1 год
        Ошибка в значении  ДС Транспортировка и хранение, тыс. руб. за  Y-2 год
        Ошибка в значении  ДС Оптовая и розничная торговля, тыс. руб. за  Y-3 год
        True

    '''

    found_empty = False
    for string in data_frame_object.values:
        for el_index, element in enumerate(string[1:]):
            if pandas.isna(element):
                found_empty = True
                print(f"Ошибка в значении  {string[0]} за  {data_frame_object.columns[el_index + 1]} год")
    return found_empty


def is_everything_ok(file_name: pandas.DataFrame) -> bool:
    '''
        >>> is_everything_ok("wrong2.xlsx")
        Ошибка в значении  ДС Обрабатывающие производства, тыс. руб. за  Y-1 год
        Ошибка в значении  ДС Транспортировка и хранение, тыс. руб. за  Y-2 год
        Ошибка в значении  ДС Оптовая и розничная торговля, тыс. руб. за  Y-3 год
        False

        >>> is_everything_ok("wrong1.xlsx")
        С параметром на 7 строке ошибка
        False
    '''
    data_frame_object = pandas.read_excel(file_name)
    return is_titles_ok(data_frame_object) and not is_empty(data_frame_object)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
