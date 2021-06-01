import random
import struct

TEXT = """
Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной "рыбой" 
для текстов на латинице с начала XVI века/ Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает 
сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а 
также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации Здесь ваш текст.. 
Здесь ваш текст.. Здесь ваш текст
""".split()
PREP = ",.?!:;"

ARR_DIGIT = [random.randint(0, 100) for _ in range(len(TEXT))]

# не сделано

with open('files_for_task_1/binary_file.txt', 'wb') as f:
    for word, digit in list(zip(TEXT, ARR_DIGIT)):
        string = word + " " + str(digit) + ' ' + str(random.choice(PREP))
        string = f"{string.encode('utf-8')}" + "\n"
        f.write(struct.pack("i", string))


with open('files_for_task_1/binary_file.txt', 'rb') as f:
    data = f.read()
    for lines in data:
        print(struct.unpack("i", lines))
