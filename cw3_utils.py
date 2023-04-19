import json


def load_operation(oper_file):
    '''Функция загрузки операций по карте из файла'''

    with open(oper_file, 'r', encoding='utf-8') as f:
        operation_data = json.load(f)
    return operation_data