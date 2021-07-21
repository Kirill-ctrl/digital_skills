import base64
from datetime import datetime, timedelta
import time
from typing import Optional


def upload_log(data: str or dict) -> None:
    """Загружает этапы выполнения функции в файл"""
    with open('/home/kirill/PycharmProjects/course_digital/week3/tasks/logs/log.txt', mode='a') as f:
        if isinstance(data, str):
            f.write(data + '\n')
        elif isinstance(data, dict):
            for key, value in data.items():
                f.write(f"  {key}: {value}\n")
        else:
            raise TypeError


def pack_dict(string: str) -> dict:
    """
    Функция преобразует строку с разделителем в словарь. For check_token
    :param string: format-string со переданным параметром + datetime.now()
    :return: удобный для работы со временем словарь
    """
    result_datetime = None
    data = []
    for item in string.split():
        try:
            result_datetime = datetime.strptime(item, '%Y-%m-%d_%H:%M:%S')
        except ValueError:
            data.append(item)
    return {
        "data": ' '.join(data),
        "datetime": result_datetime
    }


def check_token(func):
    """
    This method return created token on base64 with timedelta 3600 seconds
    :param func: принимает на вход функцию без дополнительных параметров
    :return: результат работы wrapper (результат работы функции с токеном)
    """
    upload_log("This method return created token on base64 with timedelta 3600 seconds")

    def wrapper(self):
        """
        :param self: принимает объект - класс, с которым мы работаем
        :return: валидный токен
        """
        start = datetime.now()

        if self.token:
            decode_data = base64.b64decode(self.token.encode("UTF-8")).decode('UTF-8')
            dict_data = pack_dict(decode_data)

            if datetime.now() - dict_data['datetime'] < timedelta(seconds=5):
                upload_log('Token is valid')
                return func(self)

        upload_log('Token is not valid')

        result_datetime = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        result_str = f"{self.name} {result_datetime}"
        upload_log("Use this data for create token: ")
        upload_log(pack_dict(result_str))

        result_str = result_str.encode('UTF-8')
        encode_res = base64.b64encode(result_str)
        token = encode_res.decode('UTF-8')

        self.token = token

        upload_log(f"token: {token}")
        upload_log("Time work func: " + str(datetime.now() - start))
        upload_log('----------------------------------------------')
        return func(self)

    return wrapper


class TempToken:
    """
    Класс генерирует токен по данным
    """
    token = None

    def __init__(self,
                 name: Optional[str]):
        """
        :param name: данные для уникальности токена
        """
        self.name = name

    @check_token
    def get_token(self) -> str:
        return self.token


if __name__ == '__main__':
    tkn = TempToken(name="Kirill Pechurin ")
    test_token = tkn.get_token()
    print(test_token)
    print('-------------------------')
    time.sleep(10)
    test_token = tkn.get_token()
    print(test_token)
    print('-------------------------')
    test_token = tkn.get_token()
    print(test_token)
    print('-------------------------')
    time.sleep(10)
    test_token = tkn.get_token()
    print(test_token)
