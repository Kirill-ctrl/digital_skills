from zope.interface import implementer

from course.week6.work_with_files.commands.base_interface import BaseWorkFiles
from course.week6.work_with_files.commands.commands import GET_HISTORY, ADD_TO_HISTORY


@implementer(BaseWorkFiles)
class HistoryFileCommand:
    """The class implements the interface"""

    list_history = []

    @classmethod
    def _work_by_process_type(cls, process_type: str, file_path: str, **kwargs):
        """Single entry point and division of responsibilities"""
        if process_type == ADD_TO_HISTORY:
            return cls.add_to_history(file_path, kwargs.get('params'))
        elif process_type == GET_HISTORY:
            return cls.get_history()
        else:
            raise NotImplementedError

    @classmethod
    def set_history(cls, obj_history: list):
        """Set command history"""
        cls.list_history = obj_history

    @classmethod
    def add_to_history(cls, file_path: str, params: dict):
        """Add to existing command history"""
        params['file_path'] = file_path
        cls.list_history.append(params)

    @classmethod
    def get_history(cls):
        """Get command history"""
        return cls.list_history
