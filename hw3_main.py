from hw3_utils import BankData
#    load_operation, filter_data, formatted_data

bank_operation_file = 'operations.json'

def main():
    data = BankData(bank_operation_file)
#    data = load_operation(bank_operation_file)
#    data = filter_data(data)

    for i in range(5):
        print(data.formatted_data(data[i]))

if __name__ == '__main__':
    main()

