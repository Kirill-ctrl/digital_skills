import logging

from zope.interface import implementer

from course.week6.work_with_files.commands.arw_with_file import ARWFileCommand
from course.week6.work_with_files.commands.base_interface import BaseWorkFiles
from course.week6.work_with_files.commands.commands import READ, WRITE, APPEND, DELETE, CREATE, UPDATE_RULES, ADD_TO_HISTORY, GET_HISTORY, UNDO
from course.week6.work_with_files.commands.dc_with_file import DCFileCommand
from course.week6.work_with_files.commands.history_file import HistoryFileCommand
from course.week6.work_with_files.commands.rules_file import RulesFileCommand
from course.week6.work_with_files.commands.undo_file import UndoFileCommand


@implementer(BaseWorkFiles)
class WorkFileCommand:
    """
    The class implements the interface
    Is a single entry point for the client
    """

    file_path = None

    @classmethod
    def set_file_path(cls, file_path: str):
        """Set a file path"""
        cls.file_path = file_path

    @classmethod
    def get_file_path(cls):
        """Get exist file path"""
        return cls.file_path

    @classmethod
    def _work_by_process_type(cls, process_type: str, file_path: str = file_path, **kwargs):
        """Single entry point and division of responsibilities"""
        logging.info("I distribute between teams")
        if not kwargs.get('file') or not file_path:
            file_path = cls.get_file_path()
        if process_type == READ or process_type == WRITE or process_type == APPEND:
            return ARWFileCommand._work_by_process_type(process_type, file_path, **kwargs)
        elif process_type == DELETE or process_type == CREATE:
            return DCFileCommand._work_by_process_type(process_type, file_path, **kwargs)
        elif process_type == UPDATE_RULES:
            return RulesFileCommand._work_by_process_type(process_type, file_path, **kwargs)
        elif process_type == ADD_TO_HISTORY or process_type == GET_HISTORY:
            return HistoryFileCommand._work_by_process_type(process_type, file_path, **kwargs)
        elif process_type == UNDO:
            return UndoFileCommand._work_by_process_type(process_type, file_path, **kwargs)
        else:
            logging.error("Operation undefined")
            raise NotImplementedError

    @classmethod
    def clear_history(cls):
        """clear the history"""
        logging.info("I'm clearing the history")
        HistoryFileCommand.set_history([])
