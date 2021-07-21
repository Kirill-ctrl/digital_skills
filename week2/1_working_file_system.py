import random

TEXT = """
Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной "рыбой" 
для текстов на латинице с начала XVI века/ Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает 
сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а 
также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации Здесь ваш текст.. 
Здесь ваш текст.. Здесь ваш текст
""".split()
PREP = ",.?!:;"

ARR_DIGIT = [random.randint(0, 100) for _ in range(len(TEXT))]


def create_binary_file():
    """Заполняем файл бинарными данными"""
    with open('files_for_task_1/binary_file.txt', 'wb') as f:
        for word, digit in list(zip(TEXT, ARR_DIGIT)):
            string = word + " " + str(digit) + ' ' + str(random.choice(PREP))
            f.write(string.encode('utf-8'))
            f.write('\n'.encode('utf-8'))


def read_binary_file():
    """Читаем файл и подсчитываем строки, слова, символы"""
    counter_string = 0
    counter_symb = 0
    counter_lines = 0
    with open('files_for_task_1/binary_file.txt', 'rb') as f:
        for line in f.readlines():
            counter_lines += 1
            for obj in line.split():
                decode_obj = obj.decode('utf-8')
                if decode_obj in TEXT:
                    counter_string += 1
                    counter_symb += len(decode_obj.split())
                if decode_obj in ARR_DIGIT or decode_obj in PREP:
                    counter_symb += len(decode_obj.split())
    return counter_string, counter_symb, counter_lines


if __name__ == '__main__':
    create_binary_file()
    counter_string, counter_symb, counter_lines = read_binary_file()
    print("count string: ", counter_string)
    print("count symb: ", counter_symb)
    print("count lines: ", counter_lines)
