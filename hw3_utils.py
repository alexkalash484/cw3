import json

class BankData:

    def __init__(self, oper_file):
        self.oper_file = oper_file

    def load_operation(oper_file):
        '''Функция загрузки операций по карте из файла'''
        with open(oper_file, 'r', encoding='utf-8') as f:
            operation_data = json.load(f)
        return operation_data

    def filter_data(data):
        # new_data = []
        # for item in data:
        #    if item.get('state') == 'EXECUTED':
        #        new_data.append(item)
        data = [item for item in data if item.get('state') == 'EXECUTED']
        data = sorted(data, key=lambda item: item['date'], reverse=True)
        return data

    ef
    format_date(srt_date):
    list_date = srt_date[:10].split('-')
    return '.'.join(reversed(list_date))


    def formatted_data(item):
        item_date = format_date(item.get("date"))

        if item.get("from"):
            from_ = mask_card(item.get("from")) + ' ->'
        else:
            from_ = ''

        to_ = mask_card(item.get("to"))

        return f'{item_date} {item.get("description")}\n' \
               f'{from_} {to_}\n' \
               f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n'

