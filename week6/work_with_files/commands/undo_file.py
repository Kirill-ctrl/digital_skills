import logging
import os

from zope.interface import implementer

from course.week6.work_with_files.commands.base_interface import BaseWorkFiles
from course.week6.work_with_files.commands.commands import UNDO, APPEND, WRITE, DELETE, CREATE
from course.week6.work_with_files.commands.history_file import HistoryFileCommand


@implementer(BaseWorkFiles)
class UndoFileCommand:
    """The class implements the interface"""

    @classmethod
    def _work_by_process_type(cls, process_type: str, file_path: str, **kwargs):
        """Single entry point and division of responsibilities"""
        logging.info("roll back")
        if process_type == UNDO:
            return cls.undo_command()
        else:
            raise NotImplementedError

    @staticmethod
    def undo_command():
        """Roll back one command"""
        list_history = HistoryFileCommand.get_history()
        trash = list_history.pop(-1)
        data_for_undo = trash['kwargs']['data']
        file = trash['file_path']
        process = trash['process_type']
        if process == APPEND or process == WRITE:
            with open(file, 'r') as f:
                data = f.read()
            if data_for_undo in data:
                data = data.split('\n')
                data.remove(data_for_undo)
                data = '\n'.join(data)
            with open(file, 'w') as f:
                f.write(data)
        elif process == CREATE:
            if not os.access(file, os.F_OK):
                os.remove(file)
                logging.info('File delete')
                return file
            logging.warning('File already delete')
            return None
        elif process == DELETE:
            if not os.access(file, os.F_OK):
                with open(file, 'w+') as f:
                    pass
                logging.info('File create')
                return file
            logging.warning('File already create')
            return None
        else:
            logging.error("Family process is undefined")
            raise NotImplementedError
