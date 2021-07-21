from functools import reduce

if __name__ == '__main__':
    # Соединяет слова, преобразуя в прописной вариант
    print(reduce(lambda x, y: (x + ' ' + y).lower(), ['privet', 'mir', 'hello', 'world']))
