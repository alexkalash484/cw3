import json


def load_operation(oper_file):
    '''Функция загрузки операций по карте из файла'''

    with open(oper_file, 'r', encoding='utf-8') as f:
        operation_data = json.load(f)
    return operation_data


def filter_param_data(data):
    '''Функция выбора данных по параметру "исполнено"'''

    new_data = []
    for i in data:
        if i.get('state') == 'EXECUTED':
           new_data.append(i)

    new_data = sorted(new_data, key=lambda i: i['date'], reverse=True)
    return new_data

