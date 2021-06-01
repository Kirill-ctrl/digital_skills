import os


def struct_proj(path: str) -> None:
    """
    Выводит структуру проекта в виде дерева, а также размер файлов в байтах

    :param path: путь к корневой папке проекта
    :return: None
    """
    for base_dir, dirs, files in os.walk(path):
        if os.path.basename(base_dir):
            if '.git' not in base_dir and '.git' not in dirs:
                if '\\' not in base_dir.replace(path, ''):
                    print('--', base_dir.replace(path, ''))
                    if dirs:
                        for direc in dirs:
                            print('\t--', direc)
                            for _, _, files in os.walk(os.path.join(base_dir, direc)):
                                for file in files:
                                    print('\t\t--', file, ':', os.path.getsize(os.path.join(base_dir, direc, file)), 'B')
                    else:
                        for file in files:
                            print('\t--', file, ':', os.path.getsize(os.path.join(base_dir, file)), 'B')
        else:
            for file in files:
                print('--', file, ':', os.path.getsize(os.path.join(path, file)), 'B')


struct_proj('C:/Users/kpech/PycharmProjects/testDigitalSpectr/course/')
