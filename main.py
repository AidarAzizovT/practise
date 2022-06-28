import pandas

CORRECT_TITLES = ['ВТП Казани, млн руб.', 'Добавленная стоимость, тыс. руб.',
                  'ДС Обрабатывающие производства, тыс. руб.', 'ДС Строительство, тыс. руб.',
                  'ДС Транспортировка и хранение, тыс. руб.', 'ДС Оптовая и розничная торговля, тыс. руб.',
                  'ДС Деятельность в области информатизации и связи, тыс. руб.']


def are_titles_ok(data_frame_object: pandas.DataFrame) -> bool:
    '''
    This function checks titles, are they correct or not. If there are
    mistakes with it, function returns False and prints
    where  this mistakes are. If everything is correct,
    function returns True.

        >>> df = pandas.read_excel('wrong1.xlsx')
        >>> are_titles_ok(df)
        С параметром на 7 строке ошибка
        False

        >>> df = pandas.read_excel('wrong3.xlsx')
        >>> are_titles_ok(df)
        С параметром на 4 строке ошибка
        False

        >>> df = pandas.read_excel('correct1.xlsx')
        >>> are_titles_ok(df)
        True

        >>> df = pandas.read_excel('correct2.xlsx')
        >>> are_titles_ok(df)
        True
    '''
    found_mistake = False

    for index_tt, title in enumerate(data_frame_object.values): # user one letter for index, for example, i
        if title[0] not in CORRECT_TITLES:
            print(f'С параметром на {index_tt + 2} строке ошибка')
            found_mistake = True

    return not found_mistake


def is_empty(data_frame_object: pandas.DataFrame) -> bool:
    '''
        Function checks filling of DF object, if there
        are missing data, function returns True and prints
        where this mistake are. Else, if there aren't
        any problems, function returns False.


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
        for i, element in enumerate(string[1:]):
            if pandas.isna(element):
                found_empty = True
                print(f"Ошибка в значении  {string[0]} за  {data_frame_object.columns[i + 1]} год")
    
    return found_empty


def is_everything_ok(file_name: pandas.DataFrame) -> bool:
    '''
    Function unites 2 above created functions. We need to check,
    is data correct or not. For that, we check are
    here any problems with titles or missing data.
    Returns True, if everything is correct, else returns False.

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
    return are_titles_ok(data_frame_object) and not is_empty(data_frame_object)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
