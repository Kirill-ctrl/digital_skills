import zope.interface


class BaseWorkFiles(zope.interface.Interface):
    """The interface must be inherited by all other classes that implement it"""

    def _work_by_process_type(self, process_type: str, file_path: str, **kwargs):
        """Must be defined in each class"""
        raise NotImplementedError
