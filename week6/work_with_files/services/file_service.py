import logging

from course.week6.work_with_files.commands.work_file import WorkFileCommand


def add_history(func):
    def wrapper(self, process_type, **kwargs):
        if process_type != 'ADD_TO_HISTORY' and process_type != 'GET_HISTORY' and process_type != 'UNDO':
            logging.info('Add process to history')
            WorkFileCommand._work_by_process_type(process_type="ADD_TO_HISTORY", params={"process_type": process_type, "kwargs": kwargs}, **kwargs)
        return func(self, process_type, **kwargs)
    return wrapper


class FileService:

    def __init__(self,
                 file_path: str):
        WorkFileCommand.set_file_path(file_path=file_path)

    @add_history
    def work_to_file(self, process_type: str, **kwargs):
        return WorkFileCommand._work_by_process_type(process_type=process_type, **kwargs)


if __name__ == '__main__':
    WorkFileCommand.clear_history()
