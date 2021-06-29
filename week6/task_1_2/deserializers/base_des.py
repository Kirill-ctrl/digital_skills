import zope.interface


class BaseDeserializer(zope.interface.Interface):

    def get_deserialize(cls, data, format_des: str):
        raise NotImplementedError
