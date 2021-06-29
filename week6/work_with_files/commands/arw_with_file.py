import logging

from zope.interface import implementer

from course.week6.work_with_files.commands.base_interface import BaseWorkFiles


@implementer(BaseWorkFiles)
class ARWFileCommand:

    @classmethod
    def _work_by_process_type(cls, process_type: str, file_path: str, **kwargs):
        logging.info("The process is found, I distribute between the family of this process")
        if process_type == "APPEND":
            return cls.append_in_file(file_path=file_path, **kwargs)
        elif process_type == "READ":
            return cls.read_file(file_path=file_path)
        elif process_type == "WRITE":
            return cls.write_in_file(file_path=file_path, **kwargs)
        else:
            raise NotImplementedError

    @staticmethod
    def append_in_file(file_path: str, **kwargs):
        data = kwargs.get('data')
        if not data:
            logging.warning('Required param: data')
            return None
        with open(file_path, 'a') as file:
            file.write(data + '\n')
        return data

    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
        return data

    @staticmethod
    def write_in_file(file_path: str, **kwargs):
        data = kwargs.get('data')
        if not data:
            logging.warning('Required param: data')
            return None
        with open(file_path, 'w') as file:
            file.write(data + '\n')
        return data
