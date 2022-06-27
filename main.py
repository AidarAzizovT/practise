import pandas

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
            if filling[j] == "None":
                foundEmpty = True
    if foundEmpty == True:
        return True
    else:
        return False

def check_table():
    data_frame_object = pandas.read_excel("exmaple.xlsx")
    if is_titles_ok(data_frame_object) and not is_empty(data_frame_object):
        print("Everything is fine!")
    else:
        print("Something is not correct")

check_table()
