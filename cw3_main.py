from cw3_utils import load_operation, filter_param_data, data_output

bank_operation_file = 'operations.json'

def main():
    '''Главная функция'''
    act_data = filter_param_data(load_operation(bank_operation_file))

    for i in range(5):
        print(data_output(act_data[i]))


if __name__ == '__main__':
    main()

# alex kalash 2023