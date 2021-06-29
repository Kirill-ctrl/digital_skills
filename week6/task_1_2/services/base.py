import html
import json
import xml
from abc import ABC, abstractmethod


class BaseF(ABC):

    @abstractmethod
    def serialize_to_json(self, obj: object):
        pass

    @abstractmethod
    def serialize_to_xml(self, obj: object):
        pass

    @abstractmethod
    def serialize_to_html(self, obj: object):
        pass

    @abstractmethod
    def deserialize_from_json(self, json_obj: json):
        pass

    @abstractmethod
    def deserialize_from_xml(self, xml_obj: xml):
        pass

    @abstractmethod
    def deserialize_from_html(self, html_obj: html):
        pass
