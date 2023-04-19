from cw3_utils import load_operation, filter_param_data, card_amount_format, data_output

def test_load_operation():
    '''Функция проверки load_operation'''

    list_act= [
              {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                  "amount": "31957.58",
                  "currency": {
                    "name": "руб.",
                    "code": "RUB"
                  }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
              }
            ]
    assert load_operation('test.json') == list_act

def test_filter_param_data():
    '''Функция проверки filter_param_data. Задается часть исходного файла и небходимый вывод'''

    base_list = [
        {
            'id':1,
            'state': 'EXECUTED',
            'date': '2018-11-29T07:18:23.941293'
        },
        {
            'id': 2,
            'state': 'OPEN',
            'date': '2019-11-29T07:18:23.941293'
        },
        {
            'id': 3,
            'state': 'EXECUTED',
            'date': '2020-11-29T07:18:23.941293'
        }
    ]
    sorted_list = [
        {
            'id': 3,
            'state': 'EXECUTED',
            'date': '2020-11-29T07:18:23.941293'
        },
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2018-11-29T07:18:23.941293'
        }
    ]
    assert  filter_param_data(base_list) == sorted_list


def test_card_amount_format():
    '''Функция проверки card_amount_format. Задается формат исходного счета и скрытый'''

    assert card_amount_format('Visa Gold 7305799447374042') == 'Visa Gold 7305 79** **** 4042'
    assert card_amount_format('Maestro 3364923093037194') == 'Maestro 3364 92** **** 7194'
    assert card_amount_format('Счет 96008924215040031147') == 'Счет **1147'


def test_data_output():
    '''Функция проверки data_output. Задается формат исходного файла и необходимый'''
    dict_base = {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                  "amount": "31957.58",
                  "currency": {
                    "name": "руб.",
                    "code": "RUB"
                  }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
              }
    str_res = '26.08.2019 Перевод организации\n' \
           'Maestro 1596 83** **** 5199 -> Счет **9589\n' \
           '31957.58 руб.\n'
    assert data_output(dict_base) == str_res
