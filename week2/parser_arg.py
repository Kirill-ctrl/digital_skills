import argparse


def create_parser() -> argparse.ArgumentParser:
    """Парсер аргументов для вывода структуры проекта"""
    parser = argparse.ArgumentParser(description="For struct work dir", add_help=True)
    parser.add_argument(
        '-a',
        dest='info',
        help="""
             Use the -a arguments to display the structure: -a full prints a verbose tree, 
             everything else is just files"""
    )
    return parser
