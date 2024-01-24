import json
from src.operation import *
from config import *
import dateutil.parser


def get_depersonalized_operations(operations_cnt=5):

    dict_user_operations = read_operations()
    # фильтруем от пустых словарей
    dict_user_operations = [dict_operation for dict_operation in dict_user_operations if any(dict_operation)]

    filter_user_operations = sorted(dict_user_operations,
                                    key=lambda o: dateutil.parser.parse(o['date']), reverse=True)
    filter_user_operations = [dict_operation for dict_operation in filter_user_operations
                              if dict_operation['state'] == 'EXECUTED']

    user_operations = []
    # операция в БД может быть и меньше, оставляем не более operations_cnt шт.
    for dict_operation in filter_user_operations[:operations_cnt]:

        user_operations.append(
            Operation(dict_operation['id'], dict_operation['date'],
                      dict_operation['description'], dict_operation.get('from', ''),
                      dict_operation['to'], dict_operation['operationAmount']['amount'],
                      dict_operation['operationAmount']['currency']['name']))

    # Убираем персональные данные пользователей
    for operation in user_operations:
        operation.depersonalize()

    return user_operations


def read_operations():
    with open(DB_OPERATIONS_PATH, encoding="utf-8") as file:
        json_operations = file.read()
    return json.loads(json_operations)


def print_operations(user_operations):
    for operation in user_operations:
        print(operation)
