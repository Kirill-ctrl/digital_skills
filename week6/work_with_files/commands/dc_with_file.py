import logging
import os

from zope.interface import implementer

from course.week6.work_with_files.commands.base_interface import BaseWorkFiles


@implementer(BaseWorkFiles)
class DCFileCommand:

    @classmethod
    def _work_by_process_type(cls, process_type: str, file_path: str, **kwargs):
        logging.info("The process is found, I distribute between the family of this process")
        if process_type == "DELETE":
            return cls.delete_file(**kwargs)
        elif process_type == "CREATE":
            return cls.create_file(**kwargs)
        else:
            raise NotImplementedError

    @staticmethod
    def create_file(**kwargs):
        with open(kwargs.get('file'), 'w+') as f:
            pass
        return kwargs.get('file')

    @staticmethod
    def delete_file(**kwargs):
        if os.access(kwargs.get('file'), os.F_OK):
            os.remove(kwargs.get('file'))
            return kwargs.get('file')
        logging.warning('File is not found')
        return None
