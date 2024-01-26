import pytest
from src.operation import Operation


@pytest.fixture
def operation_1():
    return Operation("1",
                     "2024-02-13T04:43:11.374324",
                     "Перевод 1",
                     "",
                     "Счет 66666011456314142963",
                     1_000_000,
                     "руб.")


@pytest.fixture
def operation_2():
    return Operation("2",
                     "2023-03-13T04:43:12.374324",
                     "Перевод 2",
                     "Счет 44444668439560358409",
                     "Счет 11111011456314142963",
                     200,
                     "USD")


@pytest.fixture
def operation_3():
    return Operation("3",
                     "2022-04-13T04:43:10.374324",
                     "Перевод 3",
                     "Maestro 1308795367077170",
                     "Счет 22222011456314142963",
                     1000.20,
                     "USD")


@pytest.mark.parametrize('operation, expected',
                         [("operation_1", f"2024-02-13T04:43:11.374324 Перевод 1\n"
                                          f" -> Счет 66666011456314142963\n"
                                          f"1000000 руб.\n"),
                          ("operation_2", f"2023-03-13T04:43:12.374324 Перевод 2\n"
                                          f"Счет 44444668439560358409 -> Счет 11111011456314142963\n"
                                          f"200 USD\n"),
                          ("operation_3", f"2022-04-13T04:43:10.374324 Перевод 3\n"
                                          f"Maestro 1308795367077170 -> Счет 22222011456314142963\n"
                                          f"1000.2 USD\n")
                          ])
def test_operation_to_str(operation, expected, request):
    operation = request.getfixturevalue(operation)
    assert operation.__str__() == expected


@pytest.mark.parametrize('operation, expected',
                         [("operation_1", f"Operation(_id=1, _date=2024-02-13T04:43:11.374324, description=Перевод 1,\n"
                                          f"send_from=, send_to=Счет 66666011456314142963,\n"
                                          f"amount=1000000, name=руб.)\n"),
                          ("operation_2", f"Operation(_id=2, _date=2023-03-13T04:43:12.374324, description=Перевод 2,\n"
                                          f"send_from=Счет 44444668439560358409, send_to=Счет 11111011456314142963,\n"
                                          f"amount=200, name=USD)\n"),
                          ("operation_3", f"Operation(_id=3, _date=2022-04-13T04:43:10.374324, description=Перевод 3,\n"
                                          f"send_from=Maestro 1308795367077170, send_to=Счет 22222011456314142963,\n"
                                          f"amount=1000.2, name=USD)\n")
                          ])
def test_operation_repr(operation, expected, request):
    operation = request.getfixturevalue(operation)
    assert operation.__repr__() == expected


@pytest.mark.parametrize('operation, expected',
                         [("operation_1", f"13.02.2024 Перевод 1\n"
                                          f" -> Счет **2963\n"
                                          f"1000000 руб.\n"),
                          ("operation_2", f"13.03.2023 Перевод 2\n"
                                          f"Счет **8409 -> Счет **2963\n"
                                          f"200 USD\n"),
                          ("operation_3", f"13.04.2022 Перевод 3\n"
                                          f"Maestro 1308 79** **** 7170 -> Счет **2963\n"
                                          f"1000.2 USD\n")
                          ])
def test_operation_depersonalize(operation, expected, request):
    operation = request.getfixturevalue(operation)
    operation.depersonalize()
    assert operation.__str__() == expected
