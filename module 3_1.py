calls = 0


def count_calls():
    #   '''функция, подсчитывающая вызовы остальных функций'''

    global calls
    calls += 1


def string_info(string):
    #   '''ф-я принимает аргумент - строку и возвращает кортеж из значений длины этой строки,
    #   этой строки в верхнем регистре и этой строки в нижнем регистре'''

    count_calls()
    string = (len(string), string.upper(), string.lower())
    return string


print(string_info('Capybara'))
print(string_info('Armageddon'))


def is_contains(string, list_to_search):
    #   '''принимает 2 аргумента: строку и список и возвращает True, если строка находится в
    #   этом списке и False, если остутствует. Регистром строки при проверке пренебречь'''

    count_calls()
    list = [i.lower() for i in list_to_search]
    return string.lower() in list
# list_to_search.count(string)


print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # no matches


print(calls)
