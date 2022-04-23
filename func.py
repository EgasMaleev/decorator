import datetime
def write_in_file(func):
    def write(listik):
        date = datetime.datetime.now()
        result = func(listik)
        name = func.__name__
        with open('generator.txt', 'w', encoding='utf-8') as file:
            file.write(f'Время -{date}\n')
            file.write(f'Имя функции -{name}\n')
            file.write(f'Результат кода -{result}\n')
            return (result)
    return(write)

@write_in_file
def MyGenerator(listik):
    for item in listik:
        for el in item:
            yield el

nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

if __name__ == '__main__':
    MyGenerator(nested_list)