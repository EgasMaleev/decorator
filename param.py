import requests
import datetime
path = 'param.txt'
def write_in_file(func):
    def write(url):
        date = datetime.datetime.now()
        result = func(url)
        name = func.__name__
        with open(path, 'w', encoding='utf-8') as file:
            file.write(f'Время -{date}\n')
            file.write(f'Имя функции -{name}\n')
            file.write(f'Результат кода -{result}\n')
            return (result)
    return(write)

@write_in_file
def get_status(url):
    response = requests.get(url=url)
    status = response.status_code
    return status


if __name__ == '__main__':
    get_status('https://yandex.ru')
