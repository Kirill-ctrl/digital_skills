import os
import sys
import parser_arg


def struct_proj(path: str) -> None:
    """
    Выводит структуру проекта в виде дерева, а также размер файлов в байтах по аргументу

    :param path: путь к корневой папке проекта
    :return: None
    """
    parser = parser_arg.create_parser()
    namespace = parser.parse_args(sys.argv[1:])
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
                                    if namespace.info == 'full':
                                        print('\t\t--', file, ':', os.path.getsize(os.path.join(base_dir, direc, file)), 'B')
                                    else:
                                        print('\t\t--', file)
                    else:
                        for file in files:
                            if namespace.info == 'full':
                                print('\t--', file, ':', os.path.getsize(os.path.join(base_dir, file)), 'B')
                            else:
                                print('\t--', file)
        else:
            for file in files:
                if namespace.info == 'full':
                    print('--', file, ':', os.path.getsize(os.path.join(path, file)), 'B')
                else:
                    print('--', file)


if __name__ == '__main__':
    struct_proj('C:/Users/kpech/PycharmProjects/testDigitalSpectr/course/')
