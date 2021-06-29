import zope.interface


class BaseWorkFiles(zope.interface.Interface):
    """docstring for class"""

    def _work_by_process_type(self, process_type: str, file_path: str, **kwargs):
        raise NotImplementedError
