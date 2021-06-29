import zope.interface


class BaseSerializer(zope.interface.Interface):

    def get_serialize(cls, obj, format_ser: str):
        raise NotImplementedError
