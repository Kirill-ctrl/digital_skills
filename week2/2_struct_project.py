import os
import sys
import parser_arg


def struct_project(path: str) -> None:
    """
    Выводит структуру проекта в виде дерева, а также размер файлов в байтах по аргументу

    :param path: путь к корневой папке проекта
    :return: None
    """
    parser = parser_arg.create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    for base_dir, dirs, files in os.walk(path):
        if '.git' not in base_dir and '.git' not in dirs:
            if '\\' not in base_dir.replace(path, ''):
                print('--', base_dir.replace(path, ''))
                for direc in dirs:
                    print('\t--', direc)
                    for _, _, f in os.walk(os.path.join(base_dir, direc)):
                        for file in f:
                            if namespace.info == 'full':
                                print('\t\t--', file, ':', os.path.getsize(os.path.join(base_dir, direc, file)), 'B')
                            else:
                                print('\t\t--', file)
                for f_ in files:
                    if namespace.info == 'full':
                        print('\t--', f_, ':', os.path.getsize(os.path.join(base_dir, f_)), 'B')
                    else:
                        print('\t--', f_)


if __name__ == '__main__':
    struct_project('C:/Users/kpech/PycharmProjects/testDigitalSpectr/course/')

