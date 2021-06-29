import logging
import os
import stat

from zope.interface import implementer

from course.week6.work_with_files.commands.base_interface import BaseWorkFiles
from course.week6.work_with_files.commands.commands import UPDATE_RULES


@implementer(BaseWorkFiles)
class RulesFileCommand:
    """The class implements the interface"""

    @classmethod
    def _work_by_process_type(cls, process_type: str, file_path: str, **kwargs):
        """Single entry point and division of responsibilities"""
        logging.info("The process is found, I distribute between the family of this process")
        if process_type == UPDATE_RULES:
            return cls.update_rules(file_path, **kwargs)
        else:
            raise NotImplementedError

    @staticmethod
    def update_rules(file_path: str, **kwargs):
        """Update file permissions by category"""
        if os.access(file_path, os.F_OK):
            if kwargs.get('peoples'):
                category = kwargs.get('peoples').lower()
                if category == 'owner':
                    os.chmod(file_path, stat.S_IRUSR & stat.S_IWUSR & stat.S_IXUSR)
                elif category == 'group':
                    os.chmod(file_path, stat.S_IRGRP & stat.S_IWGRP & stat.S_IXGRP)
                elif category == 'other':
                    os.chmod(file_path, stat.S_IROTH & stat.S_IWOTH & stat.S_IXOTH)
                return file_path
            logging.error("Required param: peoples")
            return
        else:
            logging.error("People family is undefined")
            raise NotImplementedError
